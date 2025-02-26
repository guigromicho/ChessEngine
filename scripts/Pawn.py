import pygame
from scripts.Peace import Piece

class Pawn(Piece):
    def __init__(self, game, pos, image, type):
        super().__init__(game, pos, image, type)
        self.first_move = True
        self.value = 1

    def move(self):
        from scripts.utils import find_cell

        if self.type == 'white' and self.selected:
            move_positions = []

            cell_1_step = find_cell((self.pos[0], self.pos[1] - 1), self.game.Board.board)
            if cell_1_step and not cell_1_step.piece:  # Ensure the square is empty
                move_positions.append((self.pos[0], self.pos[1] - 1))
                
                # Allow 2-square move if first move and both squares are clear
                cell_2_step = find_cell((self.pos[0], self.pos[1] - 2), self.game.Board.board)
                if self.first_move and cell_2_step and not cell_2_step.piece:
                    move_positions.append((self.pos[0], self.pos[1] - 2))

            for dx in [-1, 1]:
                new_x, new_y = self.pos[0] + dx, self.pos[1] - 1
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    cell = find_cell((new_x, new_y), self.game.Board.board)
                    if cell and cell.piece and cell.piece.type == 'black':  # Opponent piece
                        move_positions.append((new_x, new_y))

            for move_pos in move_positions:
                draw_x, draw_y = move_pos[0] * 80 + 40, move_pos[1] * 80 + 40
                pygame.draw.circle(self.game.screen, (100, 100, 255), (draw_x, draw_y), 15)

                move_rect = pygame.Rect(draw_x - 40, draw_y - 40, 80, 80)
                if pygame.mouse.get_pressed()[0] == 1 and move_rect.collidepoint(pygame.mouse.get_pos()):
                    # Handle capturing
                    cell_ = find_cell(move_pos, self.game.Board.board)
                    
                    # Remove captured piece
                    if cell_ and cell_.piece:  
                        self.game.Board.pieces.remove(cell_.piece)

                    # Move the pawn
                    self.pos = move_pos
                    self.draw_pos = (move_pos[0] * 80, move_pos[1] * 80)
                    self.first_move = False
                    cell_.piece = self

        # Check if the pawn has reached the end of the boardq
        if self.pos[1] == 0:
            pass