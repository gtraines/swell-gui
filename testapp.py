from swellgui import UiWindow, AppContextAbc, GuiAppAbc, \
                     KeypressEventsHandler, \
                     KeypressHandler, WindowEventsHandler
from pygame import locals as pyg_consts
from swellgui import DEFAULT_UI_CONFIG
from swellgui.uielements import Alignments, BasicLayout, Coord2D, \
                                DynamicTextGraphNode, \
                                SceneGraph, \
                                SceneGraphNode, \
                                RectangleGraphNode, \
                                RelativeDimensions, \
                                RelativeElementDescription, \
                                RelativeOffsetCoord, \
                                StaticTextGraphNode, \
                                WindowRootGraphNode


class GuiAppContext(AppContextAbc):

    def __init__(self, ui_config):
        AppContextAbc.__init__(self, ui_config)


class GuiApp(GuiAppAbc):

    def __init__(self):

        keypress_type_handler = self._get_keypress_type_handler()

        window = UiWindow(DEFAULT_UI_CONFIG)
        app_ctx = GuiAppContext(window.current_ui_config)

        app_ctx.scene_graph = BasicLayout()
        app_ctx.scene_graph.bottom_banner.add_child(
            self._get_centered_static_label_node("THIS IS THE DAWNING OF THE AGE OF AQUARIUS", .10, .30))
        GuiAppAbc.__init__(self, window, app_ctx, [keypress_type_handler, WindowEventsHandler()])

    def cleanup(self):
        return

    def _get_centered_static_label_node(self, text_content, relative_height_perc, relative_width_perc):

        y_offset = Alignments.get_center_of_dimension(relative_height_perc)
        x_offset = Alignments.get_center_of_dimension(relative_width_perc)

        text_offset_topleft = RelativeOffsetCoord(x_percent_offset=x_offset, y_percent_offset=y_offset)
        text_dimensions_offset = RelativeDimensions(height_percent=relative_height_perc,
                                                    width_percent=relative_width_perc)

        text_elem_desc = RelativeElementDescription(topleft_offset=text_offset_topleft,
                                                    relative_dimensions=text_dimensions_offset,
                                                    relative_layer=1)
        static_text_node = StaticTextGraphNode(text_content, text_elem_desc, None, None)
        return static_text_node

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
