import pygame
from scripts.Pawn import Pawn
def load_images(filename):
    return pygame.transform.scale(pygame.image.load(filename), (80, 80))

def load_Board(fen_string, pieces, game):
    
    piece_dict = {
        'P': 'white-pawn.png',  'p': 'black-pawn.png',
        'K': 'white-king.png',  'k': 'black-king.png',
        'Q': 'white-queen.png', 'q': 'black-queen.png',
        'R': 'white-rook.png',  'r': 'black-rook.png',
        'B': 'white-bishop.png','b': 'black-bishop.png',
        'N': 'white-knight.png','n': 'black-knight.png'
    }

    row, col = 0, 0

    for char in fen_string:
        if char == '/':  
            row += 1
            col = 0  
        elif char.isdigit():
            col += int(char)
        elif char in piece_dict:
            if char =='p' or char == 'P':
                img = load_images(f'images/{piece_dict[char]}')
                if char.islower():
                    pieces.append(Pawn(game, (col, row), img, 'black'))
                else:
                    pieces.append(Pawn(game, (col, row), img, 'white'))
            col += 1
        elif char == ' ':
            break
    
    if fen_string[-1] == 'b':
        game.Board.turn = 1
    elif fen_string[-1] == 'w':
        game.Board.turn = 0
    else:
        game.Board.turn = 0


def find_peace(pos, pieces):
    for piece in pieces:
        if piece.pos == pos:
            return piece

def find_cell(pos, board):
    for cell in board:
        if cell.x == pos[0] and cell.y == pos[1]:
            return cell
