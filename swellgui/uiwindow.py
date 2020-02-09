from .abscore import UpdatableAbc

from .config import ColorsRgb
import pygame
from pygame import constants as consts


class UiWindow(UpdatableAbc):

    WINDOW_CAPTION = "TESTING"

    def __init__(self, ui_config):

        self._launched = False
        self._is_exit_requested = False
        self._screen_surface = None
        self._screen = None
        self._all_sprites = None
        self._ui_config = ui_config

    def launch_window(self, context):
        if not self._launched:
            try:
                pygame.display.init()
                pygame.font.init()
                self._screen_surface = pygame.display.set_mode(self._ui_config.ui_dimensions,
                                                               consts.HWSURFACE | consts.DOUBLEBUF | consts.RESIZABLE)
                context.set_ui_surface(self._screen_surface)
                context.reset_fps_clock()
                pygame.display.set_caption(self.WINDOW_CAPTION)
                if not self._ui_config.debug_mode_on:
                    # see https://github.com/tobykuren/rpi_lcars/issues/9
                    #             #pygame.mouse.set_visible(False)i
                    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

                # set up screen elements
                self._all_sprites = pygame.sprite.LayeredDirty()
                repr(self._all_sprites)
                self._all_sprites.UI_PLACEMENT_MODE = self._ui_config.placement_mode_on
                self._launched = True
            except Exception as cex:
                print(repr(cex))
                self._launched = False

    def close_window(self):
        self._is_exit_requested = True

    @property
    def is_running(self):
        return self._launched and pygame.display.get_init() and not self._is_exit_requested

    @property
    def current_ui_config(self):
        return self._ui_config

    def update(self, context):
        """
        :param context: populated application context containing data required by the UI components
        """
        # GET the UI elements container somehow -- maybe a parameter
        if context is not None:
            if self.is_running:
                self._update_screen_buffer(context)
                self._show_updated_screen(context)
            else:
                print('UI exiting')
        else:
            print('WARNING: No context data or context was None')

        context.fps_clock.tick(context.ui_config.refresh_rate_hz)

    def _update_screen_buffer(self, context):
        self._screen_surface = context.ui_surface
        self._all_sprites.update(self._screen_surface)
        context.scene_graph.update(context)
        # self._screen.update(self._screen_surface, self._fps_clock)
        #self._clear_screen_buffer(context)
        #self._draw_components(context)

    def _draw_components(self, context):
        # Render the text. "True" means anti-aliased text.

        text = self._font.render(context.input_message, True, ColorsRgb.WHITE)

        # Put the image of the text on the screen at 250x250
        self._screen.blit(text, [250, 250])

    def _show_updated_screen(self, context):
        pygame.display.flip()
