import pygame

class Piece():
    def __init__(self,game,pos,image):
        self.game = game
        self.pos = pos
        self.draw_pos = ((pos[0] * 80) + 40, (pos[1] * 80) + 40)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.draw_pos
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)