#!/usr/bin/python3

#import os
import sys
import pygame
from pygame.locals import *
#import time

# own classes
from colors import *
from output import *
from game import *
from player import *
import json


class mainGUI:
    """This will be the main class, for displaying the main window
    this is for the window not game play """

    def __init__(self, width=1500, height=32 * 24):
        # init the class
        pygame.init()
        self.border = 3
        self.width = width
        self.height = height + (2 * self.border)
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.playing = True
        self.friends = []
        with open("friends.json", "r") as f:
            jsontext = f.read()
            d = json.loads(jsontext)
        for friend in d['friends']:
            x = Friend(friend['name'], friend['posx'], friend['posy'],
                       friend['image'], friend['hint'], friend['visable'])
            self.friends.append(x)

        self.myfont = pygame.font.SysFont("monospace", 15)

    def mainLoop(self):
        # the main loop for the game window
        logs = LogWindow(self.width - (32 * 26) - (3 * self.border), 275)
        Game = GameWindow(32 * 26, 32 * 24)
        deltatime = 32
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # check to see if user hits the x
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:

                        if self.playing:
                            self.playing = False
                            logs.append("pause")
                        else:
                            self.playing = True
                            logs.append('Play')
                    if self.playing:

                        if event.key == pygame.K_w:
                            Game.camera_move = 1
                            logs.append("up")
                            Game.upDatePlayerDirection("north")

                        elif event.key == pygame.K_s:
                            Game.camera_move = 2
                            logs.append("down")
                            Game.upDatePlayerDirection("south")

                        elif event.key == pygame.K_a:
                            Game.camera_move = 3
                            logs.append("left")
                            Game.upDatePlayerDirection("east")

                        elif event.key == pygame.K_d:
                            Game.camera_move = 4
                            logs.append("right")
                            Game.upDatePlayerDirection("west")

                elif event.type == pygame.KEYUP:
                    Game.camera_move = 0

        #for event in pygame.event.get():

            #check these
            if Game.camera_move == 1:
                #print ((round(Game.player_x), math.floor(Game.player_y)))
                if not Game.Blocked_At((Game.player_x, Game.player_y - 1)):
                    Game.camera_y += deltatime
            elif Game.camera_move == 2:
                if not Game.Blocked_At((Game.player_x, Game.player_y + 1)):
                    Game.camera_y -= deltatime

            elif Game.camera_move == 3:
                if not Game.Blocked_At((Game.player_x - 1, Game.player_y)):
                    Game.camera_x += deltatime
            elif Game.camera_move == 4:
                if not Game.Blocked_At((Game.player_x + 1, Game.player_y)):
                    Game.camera_x -= deltatime

            self.window.fill(color.royalBlue1)
            self.window.blit(logs.logWin, (self.width - logs.width -
                        self.border, self.height - logs.height - self.border))

            Game.gameWin.fill(color.black)
            Game.drawTerrain()
            Game.drawSquare()
            self.window.blit(Game.gameWin, (self.border, self.border))

            logs.update()
            x = 10
            for friend in self.friends:
                friend.render(self.window, (self.width - logs.width -
                        self.border, x))
                text = (str(friend.name) + " I can be found at the " +
                       str(friend.hint))
                label = self.myfont.render(text, 1, (color.black))

                self.window.blit(label, (self.width - logs.width -
                        self.border + 40, x + 20))
                x += 40
            pygame.display.update()
            #self.clock.tick(60)  # make this global laster

if __name__ == "__main__":

    mainWindow = mainGUI()
    mainWindow.mainLoop()