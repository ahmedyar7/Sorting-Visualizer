import pygame
import math

pygame.init()


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
        "I - Insertion Sort | B - Bubble Sort | S - Selection Sort | Q - Quick Sort | X - Radix Sort | C - Counting ",
        1,
        draw_info.WHITE,
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
