import pygame
from pygame import locals as pyg_const
from .abscore import UpdatableAbc, EventHandlerAbc, EventTypeHandlerAbc


class ResizeWindowHandler(EventHandlerAbc):

    def handle_event(self, event, context):
        context.ui_surface = pygame.display.set_mode(event.dict['size'],
                                                     pyg_const.HWSURFACE | pyg_const.DOUBLEBUF | pyg_const.RESIZABLE)

    def can_handle(self, event):
        return hasattr(event, 'type') and event.type == pyg_const.VIDEORESIZE


class WindowEventsHandler(EventTypeHandlerAbc):

    def __init__(self):
        self.handlers = [
            ResizeWindowHandler()
        ]

    @property
    def handlers_for_event_types(self):
        return [pyg_const.VIDEORESIZE]

    def handle_events(self, events, context):
        for evt in events:
            if evt.type in self.handlers_for_event_types:
                self._try_handle_event(evt, context)

    def _try_handle_event(self, event, context):
        for handler in self.handlers:
            if handler.can_handle(event):
                handler.handle_event(event, context)


class KeypressHandler(EventHandlerAbc):

    def __init__(self, event_key, event_type, handler_lambda, keypress_modifier=None):

        self.handle = handler_lambda
        self.event_key = event_key
        self.event_type = event_type
        self.keypress_modifier = keypress_modifier
        EventHandlerAbc.__init__(self)

    def can_handle(self, event, context):
        if hasattr(event, 'mod') and event.key == self.event_key and \
                event.type == self.event_type and \
                event.mod == self.keypress_modifier:
            return True
        elif event.key == self.event_key and \
                event.type == self.event_type and self.keypress_modifier is None:
            return True

        return False

    def handle_event(self, event, context):
        try:
            self.handle(event, context)
        except Exception as handle_ex:
            print(repr(handle_ex))


class KeypressEventsHandler(EventTypeHandlerAbc):

    def __init__(self):
        self.keypress_handlers = {}

    @property
    def handlers_for_event_types(self):
        return [pyg_const.KEYDOWN, pyg_const.KEYUP]

    def handle_events(self, events, context):
        for evt in events:
            if evt.type in self.handlers_for_event_types:
                self.handle_keypress_event(evt, context)

    def handle_keypress_event(self, event, context):
        """
        The pygame.eventpygame module for interacting with events and queues queue gets pygame.KEYDOWN and pygame.KEYUP events when the keyboard buttons are pressed and released. Both events have key and mod attributes.

        key: an integer ID representing every key on the keyboard
        mod: a bitmask of all the modifier keys that were in a pressed state when the event occurred
        The pygame.KEYDOWN event has the additional attributes unicode and scancode.

        unicode: a single character string that is the fully translated character entered, this takes into account the shift and composition keys
        scancode: the platform-specific key code, which could be different from keyboard to keyboard, but is useful for key selection of weird keys like the multimedia keys
        """
        if hasattr(event, 'key') and hasattr(event, 'type'):
            if event.key in self.keypress_handlers.keys():
                self._try_handle_keypress(event, context, self.keypress_handlers[event.key])
        return True

    @staticmethod
    def _try_handle_keypress(event, context, keypress_handlers):
        for handler in keypress_handlers:
            if handler.can_handle(event, context):
                handler.handle_event(event, context)

    def add_handler(self, handler):
        self.validate_handler(handler)
        if handler.event_key not in self.keypress_handlers.keys():
            self.keypress_handlers[handler.event_key] = []

        self.keypress_handlers[handler.event_key].append(handler)

    def populate_handlers(self, handlers):
        for handler in handlers:
            self.add_handler(handler)


class InputController(UpdatableAbc):
    KEYDOWN_HANDLERS = {}

    KEYUP_HANDLERS = {}

    def __init__(self, keydown_override_handlers=None, keyup_override_handlers=None):
        self._keydown_handlers = self.KEYDOWN_HANDLERS
        self._keyup_handlers = self.KEYUP_HANDLERS

        if keydown_override_handlers:
            for keydown_key in keydown_override_handlers.keys():
                self._keydown_handlers[keydown_key] = keydown_override_handlers[keydown_key]

        if keyup_override_handlers:
            for keyup_key in keyup_override_handlers.keys():
                self._keyup_handlers[keyup_key] = keyup_override_handlers[keyup_key]

    def update(self, context):
        self.process_input_events(context)

    def process_input_events(self, context):

        for evt in context.user_input_events:
            self._process_event(evt, context)

    def _process_event(self, evt, context):

        if evt.type == pyg_const.QUIT:
            context.done = True
        # User pressed down on a key
        elif evt.type == pyg_const.KEYDOWN:
            self._process_key_down(evt, context)
        # User let up on a key
        elif evt.type == pyg_const.KEYUP:
            self._process_key_up(evt, context)

    def _process_key_down(self, evt, context):
        # Figure out if it was an arrow key. If so
        # adjust speed.
        """ examples:
            if event_key == pyg_const.K_LEFT:
                x_speed = -3
            elif event_key == pyg_const.K_RIGHT:
                x_speed = 3
            elif event_key == pyg_const.K_UP:
                y_speed = -3
            elif event_key == pyg_const.K_DOWN:
                y_speed = 3
        """
        can_handle = evt.key in self._keydown_handlers.keys()
        if can_handle:
            handle_func = self._keydown_handlers[evt.key]
            handle_func(context)
        else:
            input_message = f'Received key_down event: {str(evt.key)} without handler'
            print(input_message)
            context.input_message = input_message

    def _process_key_up(self, evt, context):
        # If it is an arrow key, reset vector back to zero
        """
        examples:
        if event_key == pyg_const.K_LEFT or event_key == pyg_const.K_RIGHT:
            x_speed = 0
        elif event_key == pyg_const.K_UP or event_key == pyg_const.K_DOWN:
            y_speed = 0
        """
        can_handle = evt.key in self._keyup_handlers.keys()
        if can_handle:
            handle_func = self._keyup_handlers[evt.key]
            handle_func(context)
        else:
            input_message = f'Received keyup event: {str(evt.key)} without handler'
            print(input_message)
            context.input_message = input_message