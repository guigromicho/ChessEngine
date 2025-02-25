import pygame
from scripts.Peace import Piece

class Rook(Piece):
    def __init__(self, game, pos, image, tipo):
        super().__init__(game, pos, image, tipo)
        self.first_move = True
        self.value = 1
    
    def move(self):
        from scripts.utils import find_cell

        