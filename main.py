import pygame
import random
import sys
from draw_information import DrawInformation
from visulizer import draw
from algorithms import *

pygame.mixer.init()

# Load the sound
transition_sound = pygame.mixer.Sound("sound.wav")


def play_sound():
    if not pygame.mixer.get_busy():
        transition_sound.play(loops=-1)  # Play the sound in a loop


def stop_sound():
    if pygame.mixer.get_busy():
        transition_sound.stop()  # Stop the sound


pygame.init()


def generate_starting_list(n, min_val, max_val) -> list:
    """This function would randomly generate the starting list for sorting"""
    return [random.randint(min_val, max_val) for _ in range(n)]


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
                stop_sound()  # Stop the sound when sorting ends

        else:
            draw(draw_information, sorting_algorithm_name, ascending)

        # Handling of events
        # This would return all the events that have occurred since the last loop ran
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                random_list = generate_starting_list(n, min_val, max_val)
                draw_information.set_list(random_list)
                sorting = False
                stop_sound()

            elif event.key == pygame.K_SPACE and not sorting:
                play_sound()  # Start the sound when sorting begins
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(
                    draw_information, ascending
                )

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algorithm_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algorithm_name = "Bubble Sort"

            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algorithm_name = "Selection Sort"

            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort
                sorting_algorithm_name = "Merge Sort"

            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algorithm_name = "Quick Sort"

            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = counting_sort
                sorting_algorithm_name = "Counting Sort"

            elif event.key == pygame.K_x and not sorting:
                sorting_algorithm = radix_sort
                sorting_algorithm_name = "Radix Sort"

            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = heap_sort
                sorting_algorithm_name = "Heap Sort"

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
