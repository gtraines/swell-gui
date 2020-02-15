from .relativeelement import Coord2D, RelativeDimensions, RelativeOffsetCoord, RelativeElementDescription
from .scenegraph import SceneGraph, SceneGraphNode
from .shapenodes import RectangleGraphNode, WindowRootGraphNode


class Alignments:

    @staticmethod
    def get_top_aligned_offset(left_offset_percent):
        return RelativeOffsetCoord(x_percent_offset=left_offset_percent, y_percent_offset=0.0)

    @staticmethod
    def get_top_aligned_centered_offset(fractional_width):
        x_offset = Alignments.get_centered_offset(fractional_width)
        return Alignments.get_top_aligned_offset(x_offset)

    @staticmethod
    def get_bottom_anchored_centered_offset(fractional_width, fractional_height):
        x_offset = Alignments.get_centered_offset(fractional_width)
        y_offset = 1.0 - fractional_height
        return RelativeOffsetCoord(x_percent_offset=x_offset, y_percent_offset=y_offset)

    @staticmethod
    def get_centered_offset(relative_fractional_width):
        remainder = 1.0 - relative_fractional_width
        return remainder / 2.0


class TopBanner(RectangleGraphNode):

    def __init__(self, relative_width, relative_height, parent, children):
        relative_dims = RelativeDimensions(height_percent=relative_height, width_percent=relative_width)
        topleft_offset = Alignments.get_top_aligned_centered_offset(relative_width)
        relative_element_desc = RelativeElementDescription(
            topleft_offset=topleft_offset,
            relative_dimensions=relative_dims,
            relative_layer=1)

        RectangleGraphNode.__init__(self, relative_element_desc, parent, children)


class BottomBanner(RectangleGraphNode):

    def __init__(self, relative_width, relative_height, parent, children):
        relative_dims = RelativeDimensions(height_percent=relative_height, width_percent=relative_width)
        topleft_offset = Alignments.get_bottom_anchored_centered_offset(relative_width, relative_height)
        relative_element_desc = RelativeElementDescription(
            topleft_offset=topleft_offset,
            relative_dimensions=relative_dims,
            relative_layer=1)

        RectangleGraphNode.__init__(self, relative_element_desc, parent, children)


class LeftPillar(RectangleGraphNode):

    def __init__(self, relative_width, parent, children):
        relative_dims = RelativeDimensions(height_percent=1.0, width_percent=relative_width)
        topleft_offset = Alignments.get_top_aligned_offset(0.0)
        relative_element_desc = RelativeElementDescription(
            topleft_offset=topleft_offset,
            relative_dimensions=relative_dims,
            relative_layer=1)

        RectangleGraphNode.__init__(self, relative_element_desc, parent, children)


class RightPillar(RectangleGraphNode):

    def __init__(self, relative_width, parent, children):
        relative_dims = RelativeDimensions(height_percent=1.0, width_percent=relative_width)

        top_left_offset = 1.0 - relative_width

        topleft_offset = Alignments.get_top_aligned_offset(top_left_offset)
        relative_element_desc = RelativeElementDescription(
            topleft_offset=topleft_offset,
            relative_dimensions=relative_dims,
            relative_layer=1)

        RectangleGraphNode.__init__(self, relative_element_desc, parent, children)


class BasicLayout(SceneGraph):

    def __init__(self):

        self._top_banner = self._get_top_banner()
        self._bottom_banner = self._get_bottom_banner()
        self._left_pillar = self._get_left_pillar()
        self._right_pillar = self._get_right_pillar()

        root_node = WindowRootGraphNode()

        root_node.add_children([self._top_banner,
                                self._bottom_banner,
                               self._left_pillar,
                               self._right_pillar])
        SceneGraph.__init__(self, root_node)

    def _get_top_banner(self):
        top_banner = TopBanner(.70, .1, None, None)
        return top_banner

    def _get_bottom_banner(self):
        bottom_banner = BottomBanner(0.7, 0.2, None, None)
        return bottom_banner

    def _get_left_pillar(self):
        left_pillar = LeftPillar(0.15, None, None)
        return left_pillar

    def _get_right_pillar(self):
        right_pillar = RightPillar(0.15, None, None)
        return right_pillar

    @property
    def bottom_banner(self):
        return self._bottom_banner

    @property
    def top_banner(self):
        return self._top_banner

    @property
    def left_pillar(self):
        return self._left_pillar

    @property
    def right_pillar(self):
        return self._right_pillar




