from abc import ABCMeta, abstractmethod, abstractproperty


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

    @abstractproperty
    def handlers_for_event_types(self):
        pass

    @abstractmethod
    def handle_events(self, events, context):
        pass
