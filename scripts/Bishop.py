import pygame
from scripts.Peace import Piece

DIRECTIONS = [(-1, -1), (1, 1), (-1, 1), (1, -1)]  # Movimentos diagonais

class Bishop(Piece):
    def __init__(self, game, pos, image, type):
        super().__init__(game, pos, image, type)
        self.value = 3
        self.name = 'Bishop'

    def move(self):
        from scripts.utils import find_cell

        # Verifica se é o turno da peça correta e se ela está selecionada
        if ((self.game.Board.turn % 2 == 0 and self.type == "white") or 
            (self.game.Board.turn % 2 == 1 and self.type == "black")) and self.selected:

            legal_moves = []

            # Gera todos os movimentos possíveis nas diagonais
            for direction in DIRECTIONS:
                for i in range(1, 8):  # O bispo pode se mover no máximo 7 casas
                    new_x, new_y = self.pos[0] + direction[0] * i, self.pos[1] + direction[1] * i
                    cell = find_cell((new_x, new_y), self.game.Board.board)

                    if cell:
                        if not cell.piece:  # Casa vazia, pode mover
                            legal_moves.append((new_x, new_y))
                        elif cell.piece.type != self.type:  # Peça inimiga, pode capturar
                            legal_moves.append((new_x, new_y))
                            break  # Para ao capturar
                        else:  # Bloqueado por peça da mesma cor
                            break
                    else:
                        break  # Sai do tabuleiro

            # Desenha os movimentos possíveis na tela
            for move in legal_moves:
                draw_x, draw_y = move[0] * 80 + 40, move[1] * 80 + 40
                pygame.draw.circle(self.game.screen, (100, 100, 255), (draw_x, draw_y), 15)

                move_rect = pygame.Rect(draw_x - 40, draw_y - 40, 80, 80)
                if move_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:  
                    cell_ = find_cell(move, self.game.Board.board)

                    # Captura a peça adversária se houver uma
                    if cell_ and cell_.piece:
                        self.game.Board.pieces.remove(cell_.piece)

                    # Atualiza a posição do bispo
                    self.pos = move 
                    self.draw_pos = (move[0] * 80, move[1] * 80)
                    cell_.piece = self  

                    # Passa o turno após o movimento
                    self.selected = False
                    self.game.Board.turn += 1
