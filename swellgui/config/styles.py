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
    def __init__(self, background_color, foreground_color, **kwargs):
        self._style_dict = {
            'color': background_color,
            'border_color': foreground_color,
            'border_hover_color': pg.Color('yellow'),
            "clicked_color": None,
            "clicked_font_color": None,
            "click_sound": None,
            "font": 'Calibri',
            "font_size": 12,
            "font_color": foreground_color,
            "hover_color": None,
            "hover_font_color": None,
            "hover_sound": None,
            'disabled_color': pg.Color('grey'),
            'radius': 3
        }

        for arg_key in kwargs.keys():
            self._style_dict[arg_key] = kwargs[arg_key]

    def get_value(self, value_key):
        if value_key in self._style_dict.keys():
            return self._style_dict[value_key]
        print('Attempted to retrieve a style key that did not exist: ' + value_key)
        self._style_dict[value_key] = None
        return None

    def get_pg_font(self):
        return pg.font.SysFont(self._style_dict['font'], self._style_dict['font_size'], True, False)

    def set_font(self, font_name, font_size, font_color, hover_font_color=None):
        self._style_dict['font'] = font_name
        self._style_dict['font_size'] = font_size
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
