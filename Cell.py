import pygame

class Cell:
    def __init__(self, game,color1, x, y, width):
        self.color1 = color1
        self.x = x
        self.y = y
        self.width = width
        self.game = game
        self.rect = pygame.Rect(self.x * self.width ,self.y * self.width, self.width, self.width)

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color1, self.rect)