import pygame
import random
import math

pygame.init()


class DrawInfo:

    RED = 255, 0, 0
    GREEN = 0, 255, 0
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0

    BACKGROUND_COLOR = BLACK
    GRADIENT = [GREEN]

    SIDE_PADDING = 100
    TOP_PADDING = 150

    SMALL_FONT = pygame.font.SysFont("Aptos", 23)
    LARGE_FONT = pygame.font.SysFont("Aptos", 30)

    def __init__(self, width, height, list) -> None:
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithms Visualizer")

        self.set_list(list)

    def set_list(self, list) -> None:
        "This function would set the list to the screen"

        self.list = list
        self.max_value = max(self.list)
        self.min_value = min(self.list)

        self.block_width = (self.width - self.SIDE_PADDING) // len(self.list)
        self.block_height = math.floor(
            (self.height - self.TOP_PADDING) / (self.max_value - self.min_value)
        )

        self.start_x = (self.width - (self.block_width * len(list))) // 2
