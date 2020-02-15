from typing import Tuple, Optional, Any
from .spriteelement import SpriteElementBase
from .relativeelement import RelativeElementAbc
from .shapenodes import RectangleElement, RectangleGraphNode
import pygame
from pygame.color import Color
from pygame.math import Vector2
from pygame.rect import Rect


class BackgroundGrid(RectangleElement):

    def __init__(self, line_color: Color, grid_count: int):
        self._grid_count = grid_count
        self._line_color = line_color

    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):
        self.absolute_element = Rect((topleft_coords.x,
                                     topleft_coords.y),
                                     (absolute_dimensions.width,
                                     absolute_dimensions.height))

        for x in range(0, self._screen_resolution[0], self._cell_width):
            pygame.draw.line(context.ui_surface,
                             self._line_color,
                             (x, 0),
                             (x, self._screen_resolution[1]))

        for y in range(0, self._screen_resolution[1], self._cell_width):
            pygame.draw.line(surface, self._line_color, (0, y), (self._screen_resolution[0], y))


class LcarsBackground(SpriteElementBase):
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass


class LcarsBackgroundImage(SpriteElementBase):
    def __init__(self, image, ui_config):
        self.image = pygame.image.load(image).convert()
        SpriteElementBase.__init__(self, None, (0,0), None, ui_config)
    
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass


class LcarsImage(SpriteElementBase):
    def __init__(self, image, pos, ui_config):
        self.image = pygame.image.load(image).convert()
        SpriteElementBase.__init__(self, None, pos, None, ui_config)
