from .updatableabc import UpdatableAbc
from .appcontextabc import AppContextAbc
from .drawableabc import DrawableAbc
from .eventhandlerabc import EventTypeHandlerAbc, EventHandlerAbc


class Validations:

    @staticmethod
    def assert_is_updatable(candidate):
        if not isinstance(candidate, UpdatableAbc):
            raise Exception('Object must implement UpdatableAbc')

    @staticmethod
    def assert_is_appcontext(candidate):
        if not isinstance(candidate, AppContextAbc):
            raise Exception('Object must implement AppContextAbc')

    @staticmethod
    def assert_is_eventtypehandler(candidate):
        if not isinstance(candidate, EventTypeHandlerAbc):
            raise Exception('Object must implement EventTypeHandlerAbc')

    @staticmethod
    def assert_is_eventhandler(candidate):
        if not isinstance(candidate, EventHandlerAbc):
            raise Exception('Object must implement EventHandlerAbc')

    @staticmethod
    def assert_is_drawable(candidate):
        if not isinstance(candidate, DrawableAbc):
            raise Exception('Object must implement DrawableAbc')
