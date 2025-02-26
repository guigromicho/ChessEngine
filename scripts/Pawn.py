import pygame
from scripts.Peace import Piece

class Pawn(Piece):
    def __init__(self, game, pos, image, type):
        super().__init__(game, pos, image, type)
        self.value = 1
        self.first_move = True
        self.orientacao = -1 if self.type == 'white' else 1  # Brancas sobem (-1), Pretas descem (+1)
        self.name = 'Pawn'

    def move(self):
        from scripts.utils import find_cell

        if self.type == 'white' and self.pos[1] != 6:
            self.first_move = False
        if self.type == 'black' and self.pos[1] != 1:
            self.first_move = False

        # Verifica se é o turno correto
        if (self.game.Board.turn % 2 == 0 and self.type == 'white') or (self.game.Board.turn % 2 == 1 and self.type == 'black'):
            if self.selected:
                legal_moves = []

                new_y = self.pos[1] + self.orientacao
                cell_1_step = find_cell((self.pos[0], new_y), self.game.Board.board)
                if cell_1_step and not cell_1_step.piece:
                    legal_moves.append((self.pos[0], new_y))

                    if self.first_move:
                        new_y_2 = self.pos[1] + (2 * self.orientacao)
                        cell_2_step = find_cell((self.pos[0], new_y_2), self.game.Board.board)
                        if cell_2_step and not cell_2_step.piece:
                            legal_moves.append((self.pos[0], new_y_2))

                # Captura diagonal
                for dx in [-1, 1]:  # Esquerda e direita
                    new_x, new_y = self.pos[0] + dx, self.pos[1] + self.orientacao
                    if 0 <= new_x < 8 and 0 <= new_y < 8:
                        cell = find_cell((new_x, new_y), self.game.Board.board)
                        if cell and cell.piece and cell.piece.type != self.type:
                            legal_moves.append((new_x, new_y))

                # Desenha os movimentos possíveis
                for move in legal_moves:
                    draw_x, draw_y = move[0] * 80 + 40, move[1] * 80 + 40
                    pygame.draw.circle(self.game.screen, (100, 100, 255), (draw_x, draw_y), 15)

                    move_rect = pygame.Rect(draw_x - 40, draw_y - 40, 80, 80)
                    if move_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:  
                        cell_ = find_cell(move, self.game.Board.board)

                        if cell_ and cell_.piece:
                            self.game.Board.pieces.remove(cell_.piece)

                        self.pos = move
                        self.draw_pos = (move[0] * 80, move[1] * 80)
                        self.first_move = False
                        cell_.piece = self

                        if (self.type == 'white' and self.pos[1] == 0) or (self.type == 'black' and self.pos[1] == 7):
                            self.promote()

                        self.game.Board.turn += 1

    def promote(self):
        from scripts.Queen import Queen
        self.game.Board.pieces.remove(self)
        new_queen = Queen(self.game, self.pos, self.image, self.type)
        self.game.Board.pieces.append(new_queen)
        print("chegou")
