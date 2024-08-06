import pygame
from draw_info import DrawInfo


# TODO : Make the screen black
# TODO: Write the alogrithm name with green color with large font
# TODO: Write all the other text in the white color with small font


def draw(draw_info, algorithm_name, ascending) -> None:

    # -> ALGORITHM TITLE
    algorithm_title = draw_info.LARGE_FONT.render(
        f"{algorithm_name} - {"Ascending" if ascending else "Descending"}",
        1,
        draw_info.GREEN,
    )
    draw_info.window.blit(
        algorithm_name,
        (draw_info.width / 2 - algorithm_title.get_width() / 2),
        65,
        draw_info.GREEN,
    )

    # -> Sorting Algorithms TITLE
    sorting = draw_info.SMALL_FONT.render(
        "S - Selection Sort | X - Radix Sort | M - Merge Sort | H - Heap Sort | C - Counting Sort | B - Bubble Sort | I - Insertion Sort",
        draw_info.WHITE,
    )
    draw_info.window.blit(
        algorithm_name,
        (draw_info.width / 2 - sorting.get_width() / 2),
        35,
        draw_info.WHITE,
    )

    # -> CONTROLS
    controls = draw_info.SMALL_FONT.render(
        "R - Reset | A - Ascending | D - Descending",
        draw_info.WHITE,
    )
    draw_info.window.blit(
        algorithm_name,
        (draw_info.width / 2 - controls.get_width() / 2),
        5,
        draw_info.WHITE,
    )


# TODO update the display


def draw_list(draw_info, color_positions={}, clear_bg=False):

    draw_info = DrawInfo()
    lst = draw_info.list

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PADDING / 2,
            draw_info.TOP_PADDING,
            draw_info.width - draw_info.SIDE_PADDING,
            draw_info.height - draw_info.TOP_PADDING,
        )

        pygame.rect(clear_rect, draw_info.BACKGROUND_COLOR, draw_info.window)

    for i, value in enumerate(lst):
        X = draw_info.start_x + i * draw_info.block_width
        Y = draw_info.start_x - (value - draw_info.min_value) * draw_info.block_width

        colors = draw_info.GRADIENT[i % len(draw_info.GRADIENT)]

        if i in color_positions:
            colors = color_positions[i]

        pygame.rect(
            (X, Y, draw_info.block_width, draw_info.block_height),
            colors,
            draw_info.window,
        )

    if clear_bg:
        pygame.display.update()
