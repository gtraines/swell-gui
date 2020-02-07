from abc import ABCMeta, abstractmethod


class EventHandlerAbc:

    __metaclass__ = ABCMeta

    def __init__(self, event_key, event_type):
        self.event_key = event_key
        self.event_type = event_type

    def can_handle(self, event):
        if event.key == self.event_key and event.type == self.event_type:
            return True

        return False

    @abstractmethod
    def handle_event(self, event, context):
        pass
