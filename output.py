import pygame
from colors import *
from game import *
#from src.util import Vector2


class Output(object):

    def __init__(self, surface, pos, inBuffer):
        self.pos = pos
        self.surface = surface
        self.buffer = inBuffer
        self.fontobject = pygame.font.Font(None, 24)

    def draw(self):
        self.surface.fill(color.gray)
        count = 0
        for line in self.buffer[-16:]:
            self.surface.blit(self.fontobject.render('>>  ' + line, 1,
                             (255, 255, 255)), (0, 16 * count))
            count += 1

    def append(self, message):
        self.buffer.append(message)

    def notify(self, pos, event):
        pass


class LogWindow():
    # desplay the log window
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.logWin = pygame.Surface((width, height))
        self.logOut = Output(self.logWin, (1, 1), ["Welcome to Ty's adventure"])

    def update(self):
        self.logOut.draw()

    def append(self, message):
        self.logOut.append(message)
