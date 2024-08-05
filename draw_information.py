import pygame
import random
import math

pygame.init()


# This class contains global variables as class attributes
class DrawInformation:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    RED = 255, 0, 0

    BACKGROUND_COLOR = BLACK

    SIDE_PAD = 100  # Max Padding from side i.e (50px form left & right)
    TOP_PAD = 150  # This shows the padding on the top mainly the controls

    # This contains different shades of purple
    GRADIENT = [(36, 224, 83)]

    FONT = pygame.font.SysFont("Aptos", 20)
    LARGE_FONT = pygame.font.SysFont("Aptos", 30)

    # The list will contain the starting list that we need to sort
    def __init__(self, height, width, list) -> None:
        self.width = width
        self.height = height

        # Pygame window setup
        self.window = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self, list) -> None:
        self.list = list
        self.min_value = min(list)
        self.max_value = max(list)

        # This would draw the blocks onto the screen.
        # This shows how wide the pixels should be based upon the number of blocks that are being rendered to the screen.
        # The main thing is that the greater the size of the integer, the thinner the block would render.
        # Round the value because we cannot render floating values.

        self.block_width = (self.width - self.SIDE_PAD) // len(list)

        # This shows one unit of the block's height, which depends upon the largest & the smallest number in the list.
        # The difference between the max and min values would give the range of the values in the list.
        # The greater the height, the smaller the height of the single unit.

        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_value - self.min_value)
        )
        self.start_x = (
            self.width - (self.block_width * len(list))
        ) // 2  # Center the blocks
