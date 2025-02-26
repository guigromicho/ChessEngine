import pygame
from scripts.Pawn import Pawn
from scripts.Rook import Rook
from scripts.Bishop import Bishop
from scripts.Queen import Queen
from scripts.King import King
from scripts.Knight import Knight
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
            img = load_images(f'images/{piece_dict[char]}')
            if char =='p' or char == 'P':
                if char.islower():
                    pieces.append(Pawn(game, (col, row), img, 'black'))
                else:
                    pieces.append(Pawn(game, (col, row), img, 'white'))
            elif char == 'r' or char == 'R':
                if char.islower():
                    pieces.append(Rook(game, (col, row), img, 'black'))
                else:
                    pieces.append(Rook(game, (col, row), img, 'white'))
            elif char == 'b' or char == 'B':
                if char.islower():
                    pieces.append(Bishop(game, (col, row), img, 'black'))
                else:
                    pieces.append(Bishop(game, (col, row), img, 'white'))
            elif char == 'q' or char == 'Q':
                if char.islower():
                    pieces.append(Queen(game, (col, row), img, 'black'))
                else:
                    pieces.append(Queen(game, (col, row), img, 'white'))
            elif char == 'k' or char == 'K':
                if char.islower():
                    pieces.append(King(game, (col, row), img, 'black'))
                else:
                    pieces.append(King(game, (col, row), img, 'white'))
            elif char == 'n' or char == 'N':
                if char.islower():
                    pieces.append(Knight(game, (col, row), img, 'black'))
                else:
                    pieces.append(Knight(game, (col, row), img, 'white'))
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
