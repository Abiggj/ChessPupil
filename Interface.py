import pygame
import chess
import os

pygame.font.init()

MARGIN = 20
HEIGHT, WIDTH = 800, 800
CELL_SIZE = 100
LIME = (255, 244, 79)
BLUE = (105, 141, 210)
PINK = (224, 15, 180)
BLACK = (0, 0, 0)
FILES = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
PIECE_TRANSLATION = {'P': 'WP', 'N': 'WN', 'R': 'WR', 'B': 'WB', 'Q': 'WQ', 'K': 'WK',
                     'p': 'BP', 'n': 'BN', 'r': 'BR', 'b': 'BB', 'q': 'BQ', 'k': 'BK'}
ASSETS_DIR = os.path.join(os.getcwd(), "ASSETS")
FONT = pygame.font.Font('freesansbold.ttf', 20)


class interface:
    def __init__(self):
        self.BOARD_COORDS = {}
        self.WIN = pygame.display.set_mode((WIDTH + (MARGIN * 2) + 400, HEIGHT + (MARGIN * 2)))
        self.draw_board()

    def draw_board(self):
        pygame.draw.rect(self.WIN, BLUE, pygame.Rect((MARGIN, MARGIN), (WIDTH, HEIGHT)))
        for file in range(0, 8):
            for rank in range(0, 8):
                if file % 2 == 0:
                    if rank % 2 == 0:
                        color = PINK
                        coords = ((rank * CELL_SIZE) + MARGIN, (file * CELL_SIZE) + MARGIN)
                    else:
                        color = BLUE
                        coords = ((rank * CELL_SIZE) + MARGIN, ((file + 1) * CELL_SIZE) + MARGIN)
                    pygame.draw.rect(self.WIN, PINK, pygame.Rect(coords, (CELL_SIZE, CELL_SIZE)))
                else:
                    if rank % 2 == 0:
                        color = BLUE
                    else:
                        color = PINK
                self.BOARD_COORDS[FILES[file] + str(8 - rank)] = [((file * CELL_SIZE) + MARGIN, (rank * CELL_SIZE) + MARGIN),
                                                             color]
            for x in range(0, 8):
                rect = pygame.draw.rect(self.WIN, LIME,
                                        pygame.Rect(((x * CELL_SIZE) + MARGIN + 3, 0), (CELL_SIZE - 6, MARGIN)))
                text = FONT.render(FILES[x], True, BLACK)
                self.WIN.blit(text, (rect.x+(rect.width//2) - 5, rect.y))
                rect = pygame.draw.rect(self.WIN, LIME,
                                        pygame.Rect((0, (x * CELL_SIZE) + MARGIN + 3), (MARGIN, CELL_SIZE - 6)))
                text = FONT.render(str(x), True, BLACK)
                self.WIN.blit(text, (rect.x + (rect.width//2) - 5, rect.y + (rect.height//2) - 5))

        pygame.display.update()

    def update_board(self, board_pos):
        for coord in self.BOARD_COORDS.keys():
            piece = board_pos.piece_at(chess.parse_square(coord))
            vec_coords = self.BOARD_COORDS[coord]
            pygame.draw.rect(self.WIN, vec_coords[1], pygame.Rect(vec_coords[0], (CELL_SIZE, CELL_SIZE)))
            if piece is None:
                pass
            else:
                piece_code = PIECE_TRANSLATION[str(piece)]
                piece_img = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, piece_code + '.png')),
                                                   (CELL_SIZE, CELL_SIZE))
                self.WIN.blit(piece_img, vec_coords[0])
        pygame.display.update()


if __name__ == "__main__":
    pass
