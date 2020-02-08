from abc import ABCMeta
import pygame


class AppContextAbc:
    __metaclass__ = ABCMeta

    def __init__(self, ui_config, **kwargs):
        self.ui_config = ui_config
        self.ui_surface = None
        self.user_input_events = {}
        self.update_data = {}
        self.scene_graph = None
        self.fps_clock = pygame.time.Clock()
        self.is_exit_requested = False
        self.is_exiting = False

    def set_update_data(self, data_key, data):
        self.update_data[data_key] = data

    def set_ui_surface(self, surface):
        self.ui_surface = surface

    def reset_fps_clock(self):
        self.fps_clock = pygame.time.Clock()
