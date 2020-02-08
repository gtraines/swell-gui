from abc import ABCMeta, abstractmethod


class EventHandlerAbc:

    __metaclass__ = ABCMeta

    @abstractmethod
    def can_handle(self, event):
        pass

    @abstractmethod
    def handle_event(self, event, context):
        pass


class EventTypeHandlerAbc:
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_events(self, events, context):
        pass

    @staticmethod
    def validate_handler(candidate):

        if not isinstance(candidate, EventHandlerAbc):
            raise Exception('Handlers must implement EventHandlerAbc')
