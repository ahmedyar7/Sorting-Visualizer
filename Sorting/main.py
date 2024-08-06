import pygame
import random
import sys
from visualization import Visualization
from draw_info import DrawInfo


pygame.mixer.init()

TRANSITION_SOUND = pygame.mixer.Sound("sound.wav")


def play_sound() -> None:
    if not pygame.mixer.get_busy():
        TRANSITION_SOUND.play(-1)  # Play sound in loop


def stop_sound() -> None:
    if pygame.mixer.get_busy():
        pygame.mixer.stop()


pygame.init()


def generate_starting_list(n, min_value, max_value) -> list:
    return [random.randint(min_value, max_value) for _ in range(n)]


def main():

    run = True

    clock = pygame.time.Clock()

    # -> PARAMETERS:
    N = 250
    MIN_VALUE = 0
    MAX_VALUE = 500

    random_list = generate_starting_list(N, MIN_VALUE, MAX_VALUE)

    draw_info = DrawInfo(width=1280, height=650, list=random_list)  #! Error May occur
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
                stop_sound()  # Stops sound when sorting ends
        else:
            visulization.draw(sorting_algorithm, ascending)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            elif event.type == pygame.K_r:
                random_list = generate_starting_list(N, MIN_VALUE, MAX_VALUE)
                draw_info.set_list(random_list)
                sorting = False
                stop_sound()

            elif event.type == pygame.K_SPACE and not sorting:
                play_sound()
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)


if __name__ == "__main__":
    main()
