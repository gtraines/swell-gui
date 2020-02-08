from abc import ABCMeta, abstractmethod
import pygame


class GuiAppAbc:
    __metaclass__ = ABCMeta

    def __init__(self, gui_window, context, events_handlers):
        self.gui_window = gui_window
        self.context = context
        self.events_handlers = events_handlers

    def run(self):
        self.gui_window.launch_window()
        while not self.context.is_exit_requested:
            self.set_user_inputs_on_context()
            self.handle_events()
            self.gui_window.update(self.context)

        self.end_app()

    def handle_events(self):

        for event in self.context.user_input_events:

            if self.check_for_quit_event(event):
                self.context.is_exit_requested = True
                return

        for events_handler in self.events_handlers:
            events_handler.handle_events(self.context.user_input_events, self.context)

    def set_user_inputs_on_context(self):
        self.context.user_input_events = pygame.event.get()

    def check_for_quit_event(self, event):
        if (event.type == pygame.QUIT) or \
                (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):

            return True

        return False

    def end_app(self):
        print('Requested exit')
        self.context.is_exit_requested = True
        self.context.is_exiting = True
        self.cleanup()
        self.gui_window.close_window()
        pygame.quit()

    @abstractmethod
    def cleanup(self):
        pass
