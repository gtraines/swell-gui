from swellgui import UiWindow, AppContextAbc, GuiAppAbc, \
                     KeypressEventsHandler, \
                     KeypressHandler, WindowEventsHandler
from pygame import locals as pyg_consts
from swellgui import DEFAULT_UI_CONFIG
from swellgui.uielements import Coord2D, \
                                SceneGraph, \
                                SceneGraphNode, \
                                RectangleGraphNode, \
                                RelativeDimensions, RelativeElementDescription, RelativeOffsetCoord


class GuiAppContext(AppContextAbc):

    def __init__(self, ui_config):
        AppContextAbc.__init__(self, ui_config)


class GuiApp(GuiAppAbc):

    def __init__(self):

        keypress_type_handler = self._get_keypress_type_handler()

        window = UiWindow(DEFAULT_UI_CONFIG)
        app_ctx = GuiAppContext(window.current_ui_config)
        app_ctx.scene_graph = self._get_starting_scene_graph()
        GuiAppAbc.__init__(self, window, app_ctx, [keypress_type_handler, WindowEventsHandler()])

    def cleanup(self):
        return

    @staticmethod
    def _get_starting_scene_graph():
        root_offset_topleft = RelativeOffsetCoord(x_percent_offset=0, y_percent_offset=0)
        root_dims_offset = RelativeDimensions(height_percent=.95, width_percent=.95)
        root_elem_desc = RelativeElementDescription(topleft_offset=root_offset_topleft,
                                                    relative_dimensions=root_dims_offset,
                                                    relative_layer=1)
        root_node = RectangleGraphNode(root_elem_desc, None,  None)
        scene_graph = SceneGraph(root_node)
        return scene_graph

    @staticmethod
    def _get_keypress_type_handler():
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
        return keypress_handlers


if __name__ == '__main__':
    app = GuiApp()
    app.run()
