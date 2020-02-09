import pygame
from pygame.rect import Rect
from .relativeelement import RelativeElementAbc
from .scenegraph import SceneGraphNode


class RectangleElement(RelativeElementAbc):

    def __init__(self, relative_rectangle_description):
        RelativeElementAbc.__init__(self, relative_rectangle_description)

    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):
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
        self.absolute_element = Rect((topleft_coords.y,
                                     topleft_coords.x),
                                     (absolute_dimensions.width,
                                     absolute_dimensions.height))
        pygame.draw.rect(context.ui_surface,
                         context.ui_config.default_style.get_value('border_color'),
                         self.absolute_element,
                         context.ui_config.default_style.get_value('radius'))


class RectangleGraphNode(SceneGraphNode):

    def __init__(self, relative_rectangle_description, parent, children):
        self._rectangle_desc = relative_rectangle_description
        self._rectangle_element = RectangleElement(relative_rectangle_description)

        SceneGraphNode.__init__(self, drawable_element=self._rectangle_element, parent=parent, children=children)
