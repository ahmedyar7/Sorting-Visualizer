import pygame
from draw_info import DrawInfo

pygame.init()


class Visualization:

    def __init__(self, draw_info: DrawInfo) -> None:
        self.draw_info = draw_info

    def draw(self, algorithm_name, ascending) -> None:

        algorithm_title = self.draw_info.LARGE_FONT.render(
            f"{algorithm_name} - {"Ascending" if ascending else "Descending"}",
            1,
            self.draw_info.GREEN,
        )
        self.draw_info.window.blit(
            algorithm_title,
            (self.draw_info.width / 2 - algorithm_title.get_width() / 2, 65),
        )

        sorting = self.draw_info.SMALL_FONT.render(
            "S - Selection Sort | X - Radix Sort | M - Merge Sort | H - Heap Sort | C - Counting Sort | B - Bubble Sort | I - Insertion Sort",
            1,
            self.draw_info.WHITE,
        )
        self.draw_info.window.blit(
            sorting,
            (self.draw_info.width / 2 - sorting.get_width() / 2, 35),
        )

        controls = self.draw_info.SMALL_FONT.render(
            "R - Reset | A - Ascending | D - Descending", self.draw_info.WHITE, 1
        )
        self.draw_info.window.blit(
            controls, (self.draw_info.width / 2 - controls.get_width() / 2, 5)
        )

    def draw_list(self, color_positions={}, clear_bg=False) -> None:

        lst = self.draw_info.list

        if clear_bg:
            clear_rect = (
                self.draw_info.SIDE_PADDING / 2,
                self.draw_info.TOP_PADDING,
                self.draw_info.width - self.draw_info.SIDE_PADDING,
                self.draw_info.height - self.draw_info.TOP_PADDING,
            )

            pygame.rect(
                clear_rect, self.draw_info.BACKGROUND_COLOR, self.draw_info.window
            )

        for i, value in enumerate(lst):
            X = self.draw_info.start_x + i * self.draw_info.block_width
            Y = (
                self.draw_info.start_x
                - (value - self.draw_info.min_value) * self.draw_info.block_width
            )

            colors = self.draw_info.GRADIENT[i % len(self.draw_info.GRADIENT)]

            if i in color_positions:
                colors = color_positions[i]

            pygame.rect(
                (X, Y, self.draw_info.block_width, self.draw_info.block_height),
                colors,
                self.draw_info.window,
            )

        if clear_bg:
            pygame.display.update()
