import pygame
import pygame_menu
SIZE_BLOCK = 20
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
FRAME_COLOR = (0, 255, 204)
SNAKE_COLOR = (0, 102, 0)
HEADER_COLOR = (0, 204, 153)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1
size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]



screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def drow_block(color, row, column):
    pygame.draw.rect(screen, color, (SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK, SIZE_BLOCK))

snake_block = [SnakeBlock(9, 9),]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            drow_block(color, row, column)
    for block in snake_block:
        drow_block(SNAKE_COLOR, block.x, block.y)


    pygame.display.flip()