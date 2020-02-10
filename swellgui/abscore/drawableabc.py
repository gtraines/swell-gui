from abc import ABCMeta, abstractmethod


class DrawableAbc:

    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):
        pass
