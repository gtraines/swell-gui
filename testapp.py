from swellgui import UiWindow, AppContextAbc


class GuiAppContext(AppContextAbc):

    def __init__(self, ui_config):
        AppContextAbc.__init__(self, ui_config)


if __name__ == '__main__':

    window = UiWindow()
    app_ctx = GuiAppContext(window.current_ui_config)
    while window.is_running:
        window.update(app_ctx)
