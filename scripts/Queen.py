import pygame
from scripts.Peace import Piece

DIRECTIONS = [(-1,-1), (1,1), (-1,1), (1,-1), (0,1), (0,-1), (1,0), (-1,0)]

class Queen(Piece):
    def __init__(self, game, pos, image, type):
        super().__init__(game, pos, image, type)
        self.value = 9
        self.name = 'Queen'
    
    def move(self):
        from scripts.utils import find_cell

        # Verifica se o turno pertence à cor da rainha
        if (self.game.Board.turn % 2 == 0 and self.type == 'white') or (self.game.Board.turn % 2 == 1 and self.type == 'black'):
            if self.selected:
                legal_moves = []

                # Obtém todos os movimentos legais
                for direction in DIRECTIONS:
                    for i in range(1, 8):  # A rainha pode se mover até 7 casas em qualquer direção
                        new_x, new_y = self.pos[0] + direction[0] * i, self.pos[1] + direction[1] * i
                        cell = find_cell((new_x, new_y), self.game.Board.board)

                        if cell:
                            if not cell.piece:  # Casa vazia
                                legal_moves.append((new_x, new_y))
                            elif cell.piece.type != self.type:  # Peça adversária -> Pode capturar
                                legal_moves.append((new_x, new_y))
                                break  # Para de verificar essa direção após capturar
                            else:
                                break  # Peça aliada bloqueando o caminho
                        else:
                            break  # Fora do tabuleiro

                # Desenha os movimentos possíveis
                for move in legal_moves:
                    draw_x, draw_y = move[0] * 80 + 40, move[1] * 80 + 40
                    pygame.draw.circle(self.game.screen, (100, 100, 255), (draw_x, draw_y), 15)

                    move_rect = pygame.Rect(draw_x - 40, draw_y - 40, 80, 80)
                    if move_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:  
                        cell_ = find_cell(move, self.game.Board.board)
                        
                        # Remove peça capturada, se houver
                        if cell_ and cell_.piece:
                            self.game.Board.pieces.remove(cell_.piece)
                        
                        # Atualiza a posição da rainha
                        self.pos = move 
                        self.draw_pos = (move[0] * 80, move[1] * 80)
                        cell_.piece = self
                        
                        # Passa o turno para o adversário
                        self.game.Board.turn += 1
