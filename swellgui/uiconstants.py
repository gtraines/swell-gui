import pygame
from .config import UiConfig, UiDimensions, ElementStyle, ColorsRgb


class RefreshRate:
    HIGH = 60
    LOW = 30


class WindowDimensions:
    SMALL = UiDimensions(width=800, height=480)
    MEDIUM = UiDimensions(width=1366, height=768)
    FULL_SCREEN = pygame.FULLSCREEN


DEFAULT_UI_STYLE = ElementStyle(ColorsRgb.DARK_BLUE, ColorsRgb.MAGENTA)


DEFAULT_UI_CONFIG = UiConfig(WindowDimensions.MEDIUM, DEFAULT_UI_STYLE)
