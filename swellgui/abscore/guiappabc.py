from abc import ABCMeta, abstractmethod
import pygame


class GuiAppAbc:
    __metaclass__ = ABCMeta

    def __init__(self, gui_window, context, events_handlers):
        self.gui_window = gui_window
        self._context = context
        self.events_handlers = events_handlers

    def run(self):
        self.gui_window.launch_window(self._context)
        while not self._context.is_exit_requested:
            self.set_user_inputs_on_context(self._context)
            self.handle_events(self._context)
            self.gui_window.update(self._context)

        self.end_app()

    def handle_events(self, context):

        for event in context.user_input_events:

            if self.check_for_quit_event(event):
                context.is_exit_requested = True
                return

        for events_handler in self.events_handlers:
            events_handler.handle_events(context.user_input_events, context)

    def set_user_inputs_on_context(self, context):
        context.user_input_events = pygame.event.get()

    def check_for_quit_event(self, event):
        if (event.type == pygame.QUIT) or \
                (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):

            return True

        return False

    def end_app(self):
        print('Requested exit')
        self._context.is_exit_requested = True
        self._context.is_exiting = True
        self.cleanup()
        self.gui_window.close_window()
        pygame.quit()

    @abstractmethod
    def cleanup(self):
        pass
