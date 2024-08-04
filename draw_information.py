import pygame
import random

pygame.init()


# This class contain global variable as class attributes
class DrawInformation:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0

    BACKGROUND_COLOR = BLACK

    SIDE_PAD = 100  # Max Padding from side i.e (50px form left & right)
    TOP_PAD = 150  # This shows the padding on the top mainly the controls

    # This contain different shades of gray
    GRADIENT = [
        (230, 230, 250),  # Lavender
        (216, 191, 216),  # Thistle
        (221, 160, 221),  # Plum
        (238, 130, 238),  # Violet
        (218, 112, 214),  # Orchid
        (199, 21, 133),  # Medium Violet Red
        (148, 0, 211),  # Dark Violet
        (186, 85, 211),  # Medium Orchid
        (153, 50, 204),  # Dark Orchid
        (138, 43, 226),  # Blue Violet
        (147, 112, 219),  # Medium Purple
        (128, 0, 128),  # Purple
        (75, 0, 130),  # Indigo
        (106, 90, 205),  # Slate Blue
        (72, 61, 139),  # Dark Slate Blue
        (123, 104, 238),
    ]

    # The list will contain the starting list that we need to sort
    def __init__(self, height, width, list) -> None:
        self.width = width
        self.height = height

        # Pygame window setup
        self.window = pygame.display.set_mode((height, width))

        pygame.display.set_caption("Sorting Algorithm Visulizer")
        self.set_list(list)

    def set_list(self, list) -> None:
        self.list = list
        self.min_value = min(list)
        self.max_value = max(list)

        # This would draw the block on to the screen.
        # This shows that how wide the pixel should be to based upon the length of the number of block that are being render to the screen.
        # The main thing is that the greater the size of the integer the thin the block would render
        # Round the value because we cannot render the floating values

        self.block_width = (self.width - self.SIDE_PAD) // len(list)

        # This shows one unit of the block's height, This Depends upon the largest & the smallest number in list
        # The difference b/w the max and min value would give the range of the values in the list
        # Greater the height smaller the height of the single unit

        self.block_height = round(
            (self.height - self.TOP_PAD) / (self.max_value - self.min_value)
        )
        self.start_x = self.SIDE_PAD // 2  # This would initilize the x coordinate


def draw(draw_info) -> None:
    """
    >>> draw_info = class_name
    """

    # This would fill the frame with the background color
    # Then the window goul get updated as per the color provided
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info) -> None:
    """
    >>> draw_info = class_name
    """

    # This function would take the height & x_cor of the list
    # Then we need to render the block representing the valuse
    # All the blocks should contain different colors of easy difference

    lst = draw_info.list

    # We would find out the x & y corr before making the rectagle
    # The rectange would we drawn from top to bottom
    # So then we need a larger X coordinate then the y Coordinate
    # We would compare the height with the minimum the get the idea that how much high the bar should be

    for i, val in enumerate(lst):
        X = draw_info.start_x + i * draw_info.block_width
        Y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height

        color = draw_info.GRADIENT[i % len(draw_info.GRADIENT)]

        pygame.draw.rect(
            draw_info.window,
            color,
            (X, Y, draw_info.block_width, draw_info.height),
        )


def generate_starting_list(n, min_val, max_val) -> list:
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

    draw_information = DrawInformation(height=700, width=600, list=random_list)

    while run:

        clock.tick(60)  # This is the max number of time our loop can run FPS = 60
        draw(draw_info=draw_information)

        # Handling of events
        # This would return all the event that has occured since the last loop runed
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

            if events.type != pygame.KEYDOWN:
                continue

            if events.key == pygame.K_r:
                random_list = generate_starting_list(n, min_val, max_val)
                draw_information.set_list(random_list)

    pygame.quit()


if __name__ == "__main__":
    main()
