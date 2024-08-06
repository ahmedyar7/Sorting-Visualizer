import pygame
import random
import sys
from visualization import draw, draw_list
from draw_info import DrawInfo

pygame.mixer.init()

TRANSITION_SOUND = pygame.mixer.Sound("sound.wav")


def play_sound() -> None:
    if not pygame.mixer.get_busy():
        TRANSITION_SOUND.play()


def stop_sound() -> None:
    if pygame.mixer.get_busy():
        pygame.mixer.stop()  # Play sound in loop


pygame.init()


def generate_starting_list(n, min_value, max_value) -> None:
    return [random.randint(min_value, max_value) for _ in range(n)]
