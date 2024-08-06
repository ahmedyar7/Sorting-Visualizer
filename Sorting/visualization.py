import pygame

pygame.init()


def draw(draw_info, algorithm_name, ascending) -> None:

    algorithm_title = draw_info.LARGE_FONT.render(
        f"{algorithm_name} - {"Ascending" if ascending else "Descending"}",
        -1,
        draw_info.GREEN,
    )
    draw_info.window.blit(
        algorithm_title, (draw_info.width / 2 - algorithm_title.get_width() / 2, 65)
    )

    sorting = draw_info.SMALL_FONT.render(
        "S - Selection Sort | X - Radix Sort | M - Merge Sort | H - Heap Sort | C - Counting Sort | B - Bubble Sort | I - Insertion Sort",
        -1,
        draw_info.WHITE,
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))

    controls = draw_info.SMALL_FONT.render(
        "R - Reset | A - Ascending | D - Descending",
        -1,
        draw_info.WHITE,
    )
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))

    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False) -> None:

    lst = draw_info.list

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PADDING / 2,
            draw_info.TOP_PADDING,
            draw_info.width - draw_info.SIDE_PADDING,
            draw_info.height - draw_info.TOP_PADDING,
        )

        pygame.draw.rect(clear_rect, draw_info.BACKGROUND_COLOR, draw_info.window)

    for i, value in enumerate(lst):
        X = draw_info.start_x + i * draw_info.block_width
        Y = draw_info.start_x - (value - draw_info.min_value) * draw_info.block_width

        colors = draw_info.GRADIENT[i % len(draw_info.GRADIENT)]

        if i in color_positions:
            colors = color_positions[i]

        pygame.draw.rect(
            (X, Y, draw_info.block_width, draw_info.block_height),
            colors,
            draw_info.window,
        )

    if clear_bg:
        pygame.display.update()
