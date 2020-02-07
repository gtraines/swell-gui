from abc import ABCMeta, abstractmethod


class UpdatableAbc:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self, context):
        pass


class GameLoopableAbc(UpdatableAbc):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_events(self, context):
        pass
