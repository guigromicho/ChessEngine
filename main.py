import pygame
from scripts.Cell import Cell
from scripts.Peace import Piece
from scripts.utils import *
from scripts.Board import Board
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.running = True

        self.Board = Board(self)


        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect = pygame.Rect(self.mouse_pos[0],self.mouse_pos[1], 1, 1)

        self.events = pygame.event.get()

    def run(self):
        self.Board.create_board()
        load_Board('8/pppppppp/8/8/8/8/PPPPPPPP/8', self.Board.pieces, self)
        print(self.Board.turn)
        while self.running:
            self.screen.fill((144, 244, 44))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            

            self.Board.update() 

            self.clock.tick(60)
            pygame.display.flip()

        pygame.quit()


game = Game()
game.run()