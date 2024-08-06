import pygame


# TODO : Make the screen black
# TODO: Write the alogrithm name with green color with large font
# TODO: Write all the other text in the white color with small font


def draw(draw_info, algorithm_name, ascending)->None:

    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    algorithm_title = draw_info.LARGE_FONT.render(f"{algorithm_name} - {"Ascending" if ascending else "Descending"}",1,draw_info.GREEN)
