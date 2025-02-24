import pygame
from Peace import Piece  
def load_images(filename):
    return pygame.transform.scale(pygame.image.load(filename), (80, 80))

def load_Board(fen_string, pieces, game):
    
    piece_dict = {
        'p': 'white-pawn.png',  'P': 'black-pawn.png',
        'k': 'white-king.png',  'K': 'black-king.png',
        'q': 'white-queen.png', 'Q': 'black-queen.png',
        'r': 'white-rook.png',  'R': 'black-rook.png',
        'b': 'white-bishop.png','B': 'black-bishop.png',
        'n': 'white-knight.png','N': 'black-knight.png'
    }

    row, col = 0, 0

    for char in fen_string:
        if char == '/':  
            row += 1
            col = 0  
        elif char.isdigit():
            col += int(char)
        elif char in piece_dict:
            img = load_images(f'images/{piece_dict[char]}')
            pieces.append(Piece(game, (col, row), img))
            col += 1
