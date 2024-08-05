import pygame
import random
import math

pygame.init()


# This class contains global variables as class attributes
class DrawInformation:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0

    BACKGROUND_COLOR = BLACK

    SIDE_PAD = 100  # Max Padding from side i.e (50px form left & right)
    TOP_PAD = 150  # This shows the padding on the top mainly the controls

    # This contains different shades of gray
    GRADIENT = [
        (230, 230, 250),  # Lavender
        (216, 191, 216),  # Thistle
        (221, 160, 221),
    ]

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


def draw(draw_info, algo_name, ascending) -> None:
    """
    >>> draw_info = class_name
    """

    # This would fill the frame with the background color
    # Then the window would get updated as per the color provided
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1,
        draw_info.GREEN,
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 65))

    controls = draw_info.FONT.render(
        "R - Reset | Space - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.WHITE,
    )
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))
    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort", 1, draw_info.WHITE
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))
    # Drawing in the center
    # T(Text width)/2 - W(window width)/2 = center of the screen

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False) -> None:
    """
    >>> draw_info = class_name
    """

    # This function would take the height & x_cor of the list
    # Then we need to render the block representing the values
    # All the blocks should contain different colors for easy differentiation
    lst = draw_info.list

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD // 2,
            draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD,
            draw_info.height - draw_info.TOP_PAD,
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    # We would find out the x & y coordinates before making the rectangle
    # The rectangle would be drawn from top to bottom
    # So then we need a larger X coordinate than the Y coordinate
    # We would compare the height with the minimum to get the idea of how high the bar should be

    for i, val in enumerate(lst):
        X = draw_info.start_x + i * draw_info.block_width
        Y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height

        color = draw_info.GRADIENT[i % len(draw_info.GRADIENT)]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(
            draw_info.window,
            color,
            (X, Y, draw_info.block_width, draw_info.height),
        )

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val) -> list:
    """This function would randomly generate the starting list for sorting"""

    list = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        list.append(value)

    return list


# -> Sorting algorithms


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            # It temporarily stops the execution and then resumes when function called from the same place where it yielded
            # if not  we cannot use any other keypress

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(
                    draw_info=draw_info,
                    color_positions={j: draw_info.GREEN, j + 1: draw_info.RED},
                    clear_bg=True,
                )
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i: draw_info.GREEN, i - 1: draw_info.RED}, True)
            yield True

    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if (ascending and lst[j] < lst[min_idx]) or (
                not ascending and lst[j] > lst[min_idx]
            ):
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

    return lst


def main():
    run = True

    # This shows how quickly the loop runs
    clock = pygame.time.Clock()

    n = 150
    min_val = 0
    max_val = 500
    random_list = generate_starting_list(n, min_val, max_val)

    draw_information = DrawInformation(height=650, width=1280, list=random_list)
    sorting = False
    ascending = True

    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm = bubble_sort
    sorting_algorithm_generator = None

    while run:

        # This is the max number of time our loop can run FPS = 60
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_information, sorting_algorithm_name, ascending)

        # Handling of events
        # This would return all the events that have occurred since the last loop ran
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
                sorting_algorithm_generator = sorting_algorithm(
                    draw_information, ascending
                )

            elif events.key == pygame.K_a and not sorting:
                ascending = True

            elif events.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algorithm_name = "Insertion Sort"

            elif events.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algorithm_name = "Bubble Sort"

            elif events.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algorithm_name = "Selection Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
