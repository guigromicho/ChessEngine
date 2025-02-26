import pygame
from scripts.Cell import Cell

class Board():
    def __init__(self,game):
        self.game = game
        self.board = []
        self.pieces = []
        self.turn = 0       #0 for white 1 for black
    def create_board(self):
        for i in range(8):
            for j in range(8):
                color = (100, 255, 100) if (i + j) % 2 == 0 else (100, 100, 100)
                self.board.append(Cell(self.game, color, i, j, 80))
            
    def update(self):
        self.draw()
        self.piece_update()

    def piece_update(self):
        for piece in self.pieces:
            piece.check_input()
            piece.move()
        for cell in self.board:
            cell.update()

    def draw(self):
        for cell in self.board:
            cell.draw()

        for peace in self.pieces:
            peace.draw()