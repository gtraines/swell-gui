"""Helper classes and functions needed to globally enable/disable sound"""
import pygame
from pygame.mixer import Sound


# Cannot use inheritance or decorator because pygame.mixer.Sound is a C-extension.
class SoundEffect:
    """Class wrapping ``pygame.mixer.Sound`` with the ability to enable/disable sound globally

    Use this instead of ``pygame.mixer.Sound``. The interface is fully transparent.
    """
    def __init__(self, source, ui_config):
        self._ui_config = ui_config
        if ui_config.sound_on:
            self.sound = Sound(source)

    def play(self, loops=0, maxtime=0, fade_ms=0):
        if self._ui_config:
            self.sound.play(loops, maxtime, fade_ms)

    def stop(self):
        if self._ui_config:
            self.sound.stop()

    def fadeout(self, time):
        if self._ui_config:
            self.sound.fadeout(time)

    def set_volume(self, value):
        if self._ui_config:
            self.sound.set_volume(value)

    def get_volume(self):
        if self._ui_config:
            return self.sound.get_volume()

    def get_num_channels(self):
        if self._ui_config:
            return self.sound.get_num_channels()

    def get_length(self):
        if self._ui_config:
            return self.get_length()

    def get_raw(self):
        if self._ui_config:
            return self.sound.get_raw()


def init(audio_params, sound_on=True):
    """Use this instead of ``pygame.mixer.init``"""
    if sound_on:
        pygame.mixer.init(audio_params.frequency,
                          audio_params.size,
                          audio_params.channels,
                          audio_params.buffer_size)
