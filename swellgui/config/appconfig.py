import io
from os import pathsep
from pygame import font


class AppConfig:

    FONT_FILE_EXTENSIONS = [ '.ttf' ]

    def __init__(self):
        self._font_cache = {}
        self._font_paths = []

    def add_font_path(self, folder_path, is_absolute=True, relative_start=None):
        # validate the path
        self._font_paths.append(folder_path)

    def add_font(self, font_name, font_obj):
        self._font_cache[font_name] = font_obj

    def get_font_paths(self):
        return self._font_paths

    def try_get_font(self, font_name, size=12, bold=False, italic=False):

        found_font = None

        if font_name in self._font_cache.keys():
            found_font = self._font_cache[font_name]
        else:
            for candidate_path in self._font_paths:
                found_in_path = self._try_get_font_from_path(font_name, candidate_path)
                if found_in_path is not None:
                    found_font = found_in_path
                    break

            if found_font is None:
                # one last try
                found_font = font.SysFont(font_name, bold, italic, size)
        return found_font

    def _try_get_font_from_path(self, font_name, candidate_path):
        # check folder exists
        # check files for each file.FONT_FILE_EXTENSIONS
        return None

