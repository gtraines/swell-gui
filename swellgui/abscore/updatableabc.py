from abc import ABCMeta, abstractmethod


class UpdatableAbc:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, context):
        pass

    @staticmethod
    def validate_is_updatable(candidate):
        if not isinstance(candidate, UpdatableAbc):
            raise Exception('Elements must implement UpdatableAbc')
