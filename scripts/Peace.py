import pygame

class Piece:
    def __init__(self, game, pos, image, type):
        self.type = type
        self.game = game
        self.pos = pos
        self.draw_pos = ((pos[0] * 80), (pos[1] * 80))
        self.image = image
        self.rect = pygame.Rect((self.draw_pos),(80,80))
        self.first_move = True
        self.selected = False
        self.clicked = False

    def check_input(self):
        
        self.rect = pygame.Rect((self.draw_pos),(80,80))
        if pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pygame.mouse.get_pos()) and self.clicked == False:
            for piece in self.game.Board.pieces:
                if piece != self and piece.type == 'black' and piece.selected == True:
                    piece.selected = False
            self.clicked = True
            if self.selected == False:
                self.selected = True
            else:
                self.selected = False
        
        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False
            

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
