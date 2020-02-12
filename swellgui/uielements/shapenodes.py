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
        self.absolute_element = Rect((topleft_coords.x,
                                     topleft_coords.y),
                                     (absolute_dimensions.width,
                                     absolute_dimensions.height))
        pygame.draw.rect(context.ui_surface,
                         context.ui_config.default_style.get_value('border_color'),
                         self.absolute_element,
                         context.ui_config.default_style.get_value('radius'))


class StaticTextRectangleElement(RelativeElementAbc):

    def __init__(self, relative_rectangle_description, static_text):
        self._rectangle_desc = relative_rectangle_description
        self._static_text = static_text
        RelativeElementAbc.__init__(self, relative_rectangle_description)

    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):

        # Render the text. "True" means anti-aliased text.
        style_font = context.ui_config.default_style.get_pg_font()
        style_font_color = context.ui_config.default_style.get_value('font_color')
        text = style_font.render(self._static_text, True, style_font_color)

        context.ui_surface.blit(text, [topleft_coords.x, topleft_coords.y])


class DynamicTextElement(RelativeElementAbc):

    def __init__(self, relative_rectangle_description, context_data_key, starting_text=None):
        self._rectangle_desc = relative_rectangle_description
        self._starting_text = starting_text
        self._context_data_key = context_data_key

        RelativeElementAbc.__init__(self, relative_rectangle_description)

    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):
        # Render the text. "True" means anti-aliased text.
        if context.update_data is not None and context.update_data[self._context_data_key] is not None:

            style_font = context.ui_config.default_style.get_pg_font()
            style_font_color = context.ui_config.default_style.get_value('font_color')
            text = style_font.render(context.update_data[self._context_data_key],
                                     True,
                                     style_font_color)

        context.ui_surface.blit(text, [topleft_coords.x, topleft_coords.y])


class RectangleGraphNode(SceneGraphNode):

    def __init__(self, relative_rectangle_description, parent, children):
        self._rectangle_desc = relative_rectangle_description
        self._rectangle_element = RectangleElement(relative_rectangle_description)

        SceneGraphNode.__init__(self, drawable_element=self._rectangle_element, parent=parent, children=children)


class StaticTextGraphNode(SceneGraphNode):

    def __init__(self, static_text, relative_rectangle_description, parent, children):
        self._rectangle_desc = relative_rectangle_description

        SceneGraphNode.__init__(self,
                                drawable_element=StaticTextRectangleElement(relative_rectangle_description,
                                                                            static_text),
                                parent=parent,
                                children=children)


class DynamicTextGraphNode(SceneGraphNode):

    def __init__(self, relative_rectangle_description, context_data_key, parent, children, starting_text=None):
        self._rectangle_desc = relative_rectangle_description

        SceneGraphNode.__init__(self,
                                drawable_element=DynamicTextElement(relative_rectangle_description,
                                                                    context_data_key,
                                                                    starting_text),
                                parent=parent,
                                children=children)
    # def hideInfoText(self):
    #     if self.info_text[0].visible:
    #         for sprite in self.info_text:
    #             sprite.visible = False
    #
    # def showInfoText(self):
    #     for sprite in self.info_text:
    #         sprite.visible = True
