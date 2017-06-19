import pygame
from colors import *
from pytmx import load_pygame
from player import *
import math


class GameWindow:
    # the window for the game
    def __init__(self, width, height):
        # init the class

        self.width = width
        self.height = height

        # camera controls
        self.camera_x = 0
        self.camera_y = 0
        self.camera_move = 0

        pygame.init()

        self.gameWin = pygame.Surface((self.width, self.height))
        self.gameWin
        self.player = Player("Ty")
        #self.friend = Friend("Penny", 1, 1, "graphics/penny.png", True)
        self.drawTerrain()

        self.player_w, self.player_h = self.player.width, self.player.height
        self.player_x = math.floor((self.width / 2 - self.player_w / 2 -
                                    self.camera_x) / 32)
        # print (self.player_x)
        self.player_y = math.ceil((self.height / 2 - self.player_h / 2 -
                                   self.camera_y) / 32)

    def drawSquare(self):
        self.player.render(self.gameWin, (self.width / 2 - self.player_w / 2,
                                          self.height / 2 - self.player_h / 2))

    def drawTerrain(self):
        self.Blocked = []
        tmxdata = load_pygame("main.tmx")
        self.levelWin = pygame.Surface((3200, 3200))
        for x in range(100):
            for y in range(100):
                image = tmxdata.get_tile_image(x, y, 0)

                self.levelWin.blit(image, (x * 32, y * 32))
        for x in range(100):
            for y in range(100):
                try:
                    image = tmxdata.get_tile_image(x, y, 1)
                    self.levelWin.blit(image, (x * 32, y * 32))
                except:
                    pass
        for x in range(100):
            for y in range(100):
                image = tmxdata.get_tile_image(x, y, 2)

                try:
                    self.levelWin.blit(image, (x * 32, y * 32))
                    self.Blocked.append(
                        (math.floor((x * 32 + self.camera_x) / 32),
                        math.floor((y * 32 + self.camera_y) / 32)))

                except:
                    pass

                # self.gameWin.blit(image, (self.camera_x,self.camera_y))
                # print (image)
        # self.friend.render(self.levelWin, (10 * 32, 10 * 32))
        self.gameWin.blit(self.levelWin, (self.camera_x, self.camera_y))

    def upDatePlayerDirection(self, direction):
        self.player.facing = direction

    def Blocked_At(self, pos):
        for cell in self.Blocked:
            print (cell[0], pos[0])

            if cell[0] == pos[0] and cell[1] == pos[1]:
                return True

        return False
