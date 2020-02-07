from .abscore import UpdatableAbc
from .uiconstants import DEFAULT_UI_CONFIG
import pygame
from pygame import constants as consts


class UiWindow(UpdatableAbc):

    WINDOW_CAPTION = "TESTING"

    def __init__(self, ui_config=None):

        self._launched = False
        self._is_exit_requested = False
        self._screen_surface = None
        self._screen = None
        self._fps_clock = None
        self._all_sprites = None

        self._ui_config = ui_config or DEFAULT_UI_CONFIG
        self._fps = self._ui_config.refresh_rate_hz

        self._launch_window()

    def _launch_window(self):
        if not self._launched:
            try:
                pygame.display.init()
                pygame.font.init()
                self._screen_surface = pygame.display.set_mode(self._ui_config.ui_dimensions,
                                                                consts.HWSURFACE | consts.DOUBLEBUF | consts.RESIZABLE)
                self._fps_clock = pygame.time.Clock()
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
            # each UI element updates itself from the data on the context
            self.handle_events(context)
            if self.is_running:
                self._all_sprites.update(self._screen_surface)

                #self._screen.update(self._screen_surface, self._fps_clock)
                pygame.display.update()
            else:
                print('UI exiting')
        else:
            print('WARNING: No context data or context was None')

        self._fps_clock.tick(self._fps)

    def handle_events(self, context):
        context.user_input_events = pygame.event.get()
        for event in context.user_input_events:

            if (event.type == pygame.QUIT) or \
                    (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                self._is_exit_requested = True
                pygame.quit()
                return False
        # otherwise, send the context through to the child elements
        return True
