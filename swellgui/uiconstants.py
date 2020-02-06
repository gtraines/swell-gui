import pygame
from .config import UiConfig, UiDimensions


class RefreshRate:
    HIGH = 60
    LOW = 30


class UiDimensions:
    SMALL = UiDimensions(width=800, height=480)
    MEDIUM = UiDimensions(width=1366, height=768)
    FULL_SCREEN = pygame.FULLSCREEN


DEFAULT_UI_CONFIG = UiConfig(UiDimensions.MEDIUM)
