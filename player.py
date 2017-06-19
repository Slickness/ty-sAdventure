import pygame
from colors import *

## figure out why the surface needs to be a even number of tiles'
pygame.init()


class Friend:

    def __init__(self, name, posx, posy, imageLoc, hint, visable=True):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.visable = visable
        self.hint = hint
        #self.sprite = pygame.Surface((32, 32))
        #self.sprite.fill(color.red)
        self.found = False
        self.imageLoc = imageLoc
        self.sprite = pygame.image.load(imageLoc)

    def render(self, surface, pos):
        surface.blit(self.sprite, pos)


class Player:

    def __init__(self, name):
        self.name = name
        self.facing = "south"
        self.health = 100
        self.sprite = pygame.image.load("graphics/player.png")
        #self.sprite = pygame.Surface((32,32))
        size = self.sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        # Get player faces
        self.faces = self.get_faces(self.sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)

    def get_faces(self, sprite):
        faces = {}
        size = sprite.get_size()
        tile_size = (int(size[0] / 2), int(size[1] / 2))
        south = pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA)
        south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
        faces["south"] = south
        north = pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA)
        north.blit(sprite, (0, 0), (tile_size[0], tile_size[1],
                   tile_size[0], tile_size[1]))
        faces["north"] = north
        east = pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA)
        east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
        faces["east"] = east
        west = pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA)
        west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
        faces["west"] = west

        return faces