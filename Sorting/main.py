import pygame
import random
import sys
from visualization import Visualization
from draw_info import DrawInfo
from sorting_algorithms import SortingAlgorithms


TRANSITION_SOUND = pygame.mixer.Sound("sound.wav")


class Controls:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.visual = Visualization()
        self.algo = SortingAlgorithms()

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
        N = 100
        MIN_VALUE = 0
        MAX_VALUE = 200

        random_list = self.generate_starting_list(N, MIN_VALUE, MAX_VALUE)

        draw_info = DrawInfo(width=1280, height=650, list=random_list)

        sorting = False
        ascending = True

        sorting_algorithm_name = "Bubble Sort"
        sorting_algorithm = self.algo.bubble_sort
        sorting_algorithm_generator = None

        while run:
            clock.tick(60)

            if sorting:
                try:
                    next(sorting_algorithm_generator)
                except StopIteration:
                    sorting = False
                    self.stop_sound()  # Stops sound when sorting ends
            else:
                self.visual.draw(draw_info, sorting_algorithm_name, ascending)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                if event.type != pygame.KEYDOWN:
                    continue

                elif event.key == pygame.K_r:
                    random_list = self.generate_starting_list(N, MIN_VALUE, MAX_VALUE)
                    draw_info.set_list(random_list)
                    sorting = False
                    self.stop_sound()

                elif event.key == pygame.K_SPACE and not sorting:
                    self.play_sound()
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(
                        draw_info, ascending
                    )

                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False

                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = self.algo.bubble_sort
                    sorting_algorithm_name = "Bubble Sort"

                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = self.algo.insertion_sort
                    sorting_algorithm_name = "Insertion Sort"

                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = self.algo.selection_sort
                    sorting_algorithm_name = "Selection Sort"

                elif event.key == pygame.K_m and not sorting:
                    sorting_algorithm = self.algo.merge_sort
                    sorting_algorithm_name = "Merge Sort"

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    c = Controls()
    c.driver_program()
