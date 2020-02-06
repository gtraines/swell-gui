from .colorpalette import ColorsRgb
import pygame as pg

SAMPLE_STYLE = {
    "color": pg.Color('red'),
    "text": None,
    "font": None,  # pg.font.Font(None,16),
    "call_on_release": True,
    "hover_color": None,
    "clicked_color": None,
    "font_color": pg.Color("white"),
    "hover_font_color": None,
    "clicked_font_color": None,
    "click_sound": None,
    "hover_sound": None,
    'border_color': pg.Color('black'),
    'border_hover_color': pg.Color('yellow'),
    'disabled': False,
    'disabled_color': pg.Color('grey'),
    'radius': 3,
}


class ElementStyle:
    def __init__(self, background_color, border_color):
        self._style_dict = {}
        self._style_dict['color'] = background_color
        self._style_dict['border_color'] = border_color

    def set_font(self, font_name, font_color, hover_font_color=None):
        self._style_dict['font'] = font_name
        self._style_dict['font_color'] = font_color
        self._style_dict['hover_font_color'] = hover_font_color

    def set_background_color(self, color, hover_color=None, clicked_color=None):
        self._style_dict['color'] = color
        self._style_dict['hover_color'] = hover_color
        self._style_dict['clicked_color'] = clicked_color

    def set_border_style(self, border_color, border_size, border_hover_color=None):
        self._style_dict['border_color'] = border_color
        self._style_dict['radius'] = border_size
        self._style_dict['border_hover_color'] = border_hover_color


class ShapeStyle(ElementStyle):

    def __init__(self, foreground_color, background_color):
        pass


class Background:
    BG_COLOR = ColorsRgb.BLACK


class ColorSchemeRgb:
    def __init__(self):
        self._elements_styles = {}
    
    def add_element_style(self, element_name, element_style):
        self._elements_styles[element_name] = element_style
    
    def get_element_style(self, element_name):
        if element_name in self._elements_styles.keys():
            return self._elements_styles[element_name]
        else:
            return ElementStyle()
    
    def set_color(self, element_name, rgb_scheme):
        self.add_element_style(element_name, rgb_scheme)
