import pygame
import random
import sys
from visualization import Visualization
from draw_info import DrawInfo

pygame.init()
pygame.mixer.init()

TRANSITION_SOUND = pygame.mixer.Sound("sound.wav")


class Controls:
    def __init__(self) -> None:
        pass

    def play_sound(self) -> None:
        if not pygame.mixer.get_busy():
            TRANSITION_SOUND.play(-1)  # Play sound in loop

    def stop_sound(self) -> None:
        if pygame.mixer.get_busy():
            pygame.mixer.stop()

    def generate_starting_list(self, n, min_value, max_value) -> list:
        return [random.randint(min_value, max_value) for _ in range(n)]

    def driver_program(self):

        run = True

        clock = pygame.time.Clock()

        # -> PARAMETERS:
        N = 50
        MIN_VALUE = 0
        MAX_VALUE = 100

        random_list = self.generate_starting_list(N, MIN_VALUE, MAX_VALUE)

        draw_info = DrawInfo(
            width=1280, height=650, list=random_list
        )  #! Error May occur
        visulization = Visualization(draw_info)  #! Error May occur

        sorting = False
        ascending = True

        sorting_algorithm_name = "Bubble Sort"
        sorting_algorithm_generator = None
        sorting_algorithm = ...  # bubble_sort

        while run:
            clock.tick(60)

            if sorting:
                try:
                    next(sorting_algorithm_generator)
                except StopIteration:
                    sorting = False
                    self.stop_sound()  # Stops sound when sorting ends
            else:
                visulization.draw(sorting_algorithm, ascending)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                if event.type != pygame.KEYDOWN:
                    continue

                elif event.type == pygame.K_r:
                    random_list = self.generate_starting_list(N, MIN_VALUE, MAX_VALUE)
                    draw_info.set_list(random_list)
                    sorting = False
                    self.stop_sound()

                elif event.type == pygame.K_SPACE and not sorting:
                    self.play_sound()
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(
                        draw_info, ascending
                    )


if __name__ == "__main__":
    controls = Controls()
    controls.driver_program()