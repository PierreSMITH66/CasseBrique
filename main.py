import random

import core
import pygame
from pygame.math import Vector2

import ball
import brick
import racket
import screen


def setup():

    print("Setup START--------------")
    screen.Screen()
    core.memory("player", racket.Racket)
    print("Setup END----------------")



def run():

    core.cleanScreen()
    racket.Racket.show(core.memory("player"))

core.main(setup, run)