import pygame
import random

pygame.init()


# This class contain global variable as class attributes
class DrawInformation:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    GREY = 125, 125, 125
    BACKGROUND_COLOR = WHITE
    SIDE_PAD = 100  # Max Padding from side i.e (50px form left & right)
    TOP_PAD = 150  # This shows the padding on the top mainly the controls

    # The list will contain the starting list that we need to sort
    def __init__(self, height, width, list):
        self.width = width
        self.height = height

        # Pygame window setup
        self.window = pygame.display.set_mode((height, width))
        pygame.display.set_caption("Sorting Algorithm Visulizer")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.min_value = min(list)
        self.max_value = max(list)

        # This would draw the block on to the screen.
        # This shows that how wide the pixel should be to based upon the length of the number of block that are being render to the screen.
        # The main thing is that the greater the size of the integer the thin the block would render
        # Round the value because we cannot render the floating values

        self.block_width = round((self.width - self.SIDE_PAD) / len(list))

        # This shows one unit of the block's height, This Depends upon the largest & the smallest number in list
        # The difference b/w the max and min value would give the range of the values in the list
        # Greater the height smaller the height of the single unit

        self.block_width = round(
            (self.height - self.TOP_PAD) / (self.max_value - self.min_value)
        )
        self.start_x = self.SIDE_PAD // 2  # This would initilize the x coordinate


def generate_starting_list(n, min_val, max_val):
    """This function would randomly generate the starting list for sorting"""

    list = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        list.append(value)

    return list


def main():
    run = True

    # This shows how quickly the loop runs
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    random_list = generate_starting_list(n, min_val, max_val)

    draw_information = DrawInformation(height=800, width=600, list=random_list)

    while run:

        clock.tick(60)  # This is the max number of time our loop can run FPS = 60
        pygame.display.update()

        # Handling of events
        # This would return all the event that has occured since the last loop runed
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
