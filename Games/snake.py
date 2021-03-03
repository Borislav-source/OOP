import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.start = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, position):
        self.color = color
        self.pos = position

    def move(self):
        pass

    def reset(self):
        pass

    def addCube(self):
        pass

    def draw(self):
        pass


def drawGrid(w, rows, surface):
    pass


def redrawWindow(surface):
    pass


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    pass


rows = 0
w = 0
h = 0

cube.rows = rows
cube.w = w

main()