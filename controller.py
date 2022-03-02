import imp
import pygame
from ball import Ball
from map import Map
from plat import Platform
from powerup import Powerup

class Controller :
    def __init__(self, screen, width, height) -> None:
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.map = Map()
        self.balls = [Ball(),Ball()]
        self.platforms = [Platform(), Platform()]
        self.powerups = []
