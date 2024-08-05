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
        (255, 160, 122),  # Light Salmon
        (250, 128, 114),  # Salmon
        (233, 150, 122),  # Dark Salmon
        (255, 140, 0),  # Dark Orange
        (255, 165, 0),  # Orange
        (255, 69, 0),  # Red Orange
        (255, 127, 80),  # Coral
        (255, 99, 71),  # Tomato
        (255, 114, 86),  # Sizzling Red
        (255, 115, 77),  # Outrageous Orange
        (255, 204, 92),  # Orange Yellow
        (255, 128, 0),  # Bittersweet Orange
        (255, 117, 24),  # Pumpkin
    ]

    FONT = pygame.font.SysFont("Aptos", 25)
    LARGE_FONT = pygame.font.SysFont("Aptos", 40)

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

    controls = draw_info.FONT.render(
        "R - Reset | Space - Start Sorting | A - Ascending | D - Desending",
        1,
        draw_info.WHITE,
    )
    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort", 1, draw_info.WHITE
    )
    # Drawing in the center
    # T(Text width)/2 - W(window with)/2 = center of screen
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False) -> None:
    """
    >>> draw_info = class_name
    """

    # This function would take the height & x_cor of the list
    # Then we need to render the block representing the valuse
    # All the blocks should contain different colors of easy difference

    lst = draw_info.list

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD // 2,
            draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD,
            draw_info.height - draw_info.TOP_PAD,
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    # We would find out the x & y corr before making the rectagle
    # The rectange would we drawn from top to bottom
    # So then we need a larger X coordinate then the y Coordinate
    # We would compare the height with the minimum the get the idea that how much high the bar should be

    for i, val in enumerate(lst):
        X = draw_info.start_x + i * draw_info.block_width
        Y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height

        color = draw_info.GRADIENT[i % len(draw_info.GRADIENT)]

        for i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(
            draw_info.window,
            color,
            (X, Y, draw_info.block_width, draw_info.height),
        )

    if clear_bg:
        color = color_positions[i]


def generate_starting_list(n, min_val, max_val) -> list:
    """This function would randomly generate the starting list for sorting"""

    list = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        list.append(value)

    return list


# -> Sorting algorithms


def bubble_sort(draw_info, ascending=False):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            # It temporarily stop the execution and then resume when function called from the same place where it yeilded
            # if not  we cannot use and other keypress

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # draw_list()
                yield True

    return lst


def main():
    run = True

    # This shows how quickly the loop runs
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    random_list = generate_starting_list(n, min_val, max_val)

    draw_information = DrawInformation(height=700, width=600, list=random_list)
    sorting = False
    ascending = True

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
                sorting = False

            elif events.key == pygame.K_SPACE and sorting == False:
                sorting = True

            elif events.key == pygame.K_a and not sorting:
                ascending = True

            elif events.key == pygame.K_a and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
