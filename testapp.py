from swellgui import UiWindow, AppContextAbc, GuiAppAbc, KeypressEventsHandler, KeypressHandler
from pygame import locals as pyg_consts


class GuiAppContext(AppContextAbc):

    def __init__(self, ui_config):
        AppContextAbc.__init__(self, ui_config)


class GuiApp(GuiAppAbc):

    def __init__(self):
        keypress_handlers = KeypressEventsHandler()

        keypress_handlers.add_handler(KeypressHandler(pyg_consts.K_UP,
                                                      pyg_consts.KEYDOWN,
                                                      lambda evt, ctx: ctx.set_update_data('KEYPRESS',
                                                                                           'K_UP UNMODIFIED')))
        keypress_handlers.add_handler(KeypressHandler(pyg_consts.K_UP,
                                                      pyg_consts.KEYDOWN,
                                                      lambda evt, ctx: ctx.set_update_data('KEYPRESS',
                                                                                           'K_UP SHIFT'),
                                                      keypress_modifier=pyg_consts.KMOD_LSHIFT))

        window = UiWindow()
        app_ctx = GuiAppContext(window.current_ui_config)
        GuiAppAbc.__init__(self, UiWindow(), app_ctx, [keypress_handlers])

    def cleanup(self):
        return


if __name__ == '__main__':
    app = GuiApp()
    app.run()
