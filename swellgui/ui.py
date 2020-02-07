import pygame


class UserInterface:
    def __init__(self, screen, ui_config):
        # init system
        pygame.display.init()
        pygame.font.init()
        # sound.init(ui_config.audio_params)

        self.screenSurface = pygame.display.set_mode(ui_config.ui_dimensions,
                                                     HWSURFACE | DOUBLEBUF | RESIZABLE)  # , pygame.FULLSCREEN)
        self.fpsClock = pygame.time.Clock()
        self.fps = ui_config.refresh_rate_hz

        pygame.display.set_caption("LCARS")
        if not ui_config.debug_mode_on:
            # see https://github.com/tobykuren/rpi_lcars/issues/9
            #             #pygame.mouse.set_visible(False)i
            pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

        # set up screen elements
        self.all_sprites = pygame.sprite.LayeredDirty()
        repr(self.all_sprites)
        self.all_sprites.UI_PLACEMENT_MODE = ui_config.placement_mode_on

        self.screen = screen
        self.screen.setup(self.all_sprites)
        self.running = True

    def update(self):
        self.screen.pre_update(self.screenSurface, self.fpsClock)
        self.all_sprites.update(self.screenSurface)
        self.screen.update(self.screenSurface, self.fpsClock)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
                    (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                self.running = False
                return

            for sprite in self.all_sprites.sprites():
                if hasattr(event, "pos"):
                    focussed = sprite.rect.collidepoint(event.pos)
                    if (focussed or sprite.focussed) and sprite.handleEvent(event, self.fpsClock):
                        break

            self.screen.handleEvents(event, self.fpsClock)

            newScreen = self.screen.getNextScreen()
            if (newScreen):
                self.all_sprites.empty()
                newScreen.setup(self.all_sprites)
                self.screen = newScreen
                break

    def is_running(self):
        pygame.display.get_init()

    def tick(self):
        self.update()
        self.handle_events()
        self.fpsClock.tick(self.fps)
