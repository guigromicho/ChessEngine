import pygame
from scripts.Peace import Piece

DIRECTIONS = [(-1,-1) , (1,1) , (-1,1) , (1,-1)]

class Bishop(Piece):
    def __init__(self, game, pos, image, type):
        super().__init__(game, pos, image, type)
        self.value = 3
    
    def move(self):
        from scripts.utils import find_cell

        if self.type == 'white' and self.selected:
            legal_moves = []

            #get all legal moves
            for direction in DIRECTIONS:
                for i in range(1, 8):
                    new_x, new_y = self.pos[0] + direction[0] * i, self.pos[1] + direction[1] * i
                    cell = find_cell((new_x, new_y), self.game.Board.board)

                    if cell:
                        if not cell.piece:
                            legal_moves.append((new_x, new_y))
                        elif cell.piece.type == 'black':
                            legal_moves.append((new_x, new_y))
                            break
                        else:
                            break
                    else:
                        break

            for move in legal_moves:
                draw_x, draw_y = move[0] * 80 + 40, move[1] * 80 + 40
                pygame.draw.circle(self.game.screen, (100, 100, 255), (draw_x, draw_y), 15)

                move_rect = pygame.Rect(draw_x - 40, draw_y - 40, 80, 80)
                if move_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:  
                    cell_ = find_cell(move, self.game.Board.board)
                    
                    # Remove peça capturada
                    if cell_ and cell_.piece:
                        self.game.Board.pieces.remove(cell_.piece)
                    
                    # Atualiza referência da peça no tabuleiro
                    self.pos = move 
                    self.draw_pos = (move[0] * 80, move[1] * 80)
                    self.first_move = False
                    cell_.piece = self  
