import pygame
from Cell import Cell
from Peace import Piece
from utils import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = []
        self.peaces = []

    def run(self):
        self.create_board()
        load_Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', self.peaces, self)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.clock.tick(60)
            self.screen.fill((144, 244, 44))
            
            self.draw()  
            pygame.display.flip()

        pygame.quit()

    def draw(self):
        for cell in self.board:
            cell.draw()

        for peace in self.peaces:
            peace.draw()

    def create_board(self):
        for i in range(8):
            for j in range(8):
                color = (100, 100, 100) if (i + j) % 2 == 0 else (100, 255, 100)
                self.board.append(Cell(self, color, i, j, 80))


game = Game()
game.run()