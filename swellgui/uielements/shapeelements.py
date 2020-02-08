import pygame
from .elementcontainer import RelativeElementAbc


class RelativeRectangleElement(RelativeElementAbc):

    def update(self, context):
        pass

    def __init__(self, relative_description):
        super().__init__(relative_description)

    def draw_element(self, context, topleft_coords, absolute_dimensions, layer):
        """
        pygame.draw.rect()
draw a rectangle
rect(surface, color, rect) -> Rect
rect(surface, color, rect, width=0) -> Rect
Draws a rectangle on the given surface.

Parameters:
surface (Surface) -- surface to draw on
color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
rect (Rect) -- rectangle to draw, position and dimensions
width (int) --
(optional) used for line thickness or to indicate that the rectangle is to be filled (not to be confused with the width value of the rect parameter)

if width == 0, (default) fill the rectangle
if width > 0, used for line thickness
if width < 0, nothing will be drawn
        """

        BLUE = (0, 0, 255)
        """
            Rect(left, top, width, height) -> Rect
            Rect((left, top), (width, height)) -> Rect
            Rect(object) -> Rect
        """
        pygame.draw.rect(context.display_surface, BLUE,
                         (topleft_coords.x,
                          topleft_coords.y,
                          absolute_dimensions.width,
                          absolute_dimensions.height), 10)
