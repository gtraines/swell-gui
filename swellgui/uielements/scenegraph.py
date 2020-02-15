
from ..abscore import UpdatableAbc, Validations
from .relativeelement import Coord2D, Dimensions2D, RelativeElementAbc


class SceneGraphNode(UpdatableAbc):

    def __init__(self, drawable_element=None, parent=None, children=None):

        self._drawable_element = drawable_element
        if self._drawable_element is not None:
            Validations.assert_is_drawable(self._drawable_element)

        self._parent = parent
        if self._parent is not None:
            self._parent.add_child(self)

        self._children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def update(self, context):
        if self._drawable_element is not None:
            self._draw_self(context)

        if self._children is not None and len(self._children) > 0:
            for child in self._children:
                child.update(context)

    def _draw_self(self, context):
        if self._parent is None:
            # Then it is the top-level node aka root
            dims = Dimensions2D(height=context.ui_surface.get_height(),
                                width=context.ui_surface.get_width())

            self._drawable_element.draw_absolute(
                parent_topleft_coord=Coord2D(0, 0),
                parent_dimensions=dims,
                parent_layer=0,
                context=context
            )
        else:
            self._drawable_element.draw_absolute(
                parent_topleft_coord=self._parent.get_absolute_topleft_coords(context),
                parent_dimensions=self._parent.get_absolute_dimensions(context),
                parent_layer=self._parent.get_absolute_layer(),
                context=context)

    @property
    def drawable_element(self):
        return self._drawable_element

    def get_absolute_topleft_coords(self, context):
        if self._parent is None:
            return Coord2D(0, 0)
        elif self._drawable_element is not None:

            parent_drawable_element = self._parent.drawable_element

            if parent_drawable_element is not None:
                parent_element_topleft = parent_drawable_element.get_absolute_topleft_coords(
                    self._parent.get_absolute_topleft_coords(context),
                    self._parent.get_absolute_dimensions(context)
                )

                return self._drawable_element.get_absolute_topleft_coords(
                    parent_element_topleft,
                    self._parent.get_absolute_dimensions(context))
            else:
                return self._drawable_element.get_absolute_topleft_coords(
                    self._parent.get_absolute_topleft_coords(context),
                    self._parent.get_absolute_dimensions(context))
        else:
            return self._parent.get_absolute_topleft_coords(context)

    def get_absolute_layer(self):
        if self._parent is None:
            return 0
        elif self._drawable_element is not None:
            return self._drawable_element.get_absolute_layer(self._parent.get_absolute_layer())
        else:
            return self._parent.get_absolute_layer() + 1

    def get_absolute_dimensions(self, context):
        if self._parent is None:
            # top-level (root) node; return the dimensions of the surface
            return Dimensions2D(height=context.ui_surface.get_height(),
                                width=context.ui_surface.get_width())
        elif self._drawable_element is not None:
            # we have a drawn element so we should use that as the dimensions for this node
            return self._drawable_element.get_absolute_dimensions(self._parent.get_absolute_dimensions(context))
        else:
            # we have an invisible/pass through node so use the parent
            return self._parent.get_absolute_dimensions(context)

    def set_parent(self, parent):
        self._parent = parent

    def add_child(self, child):
        self.validate_node(child)
        child.set_parent(self)
        self._children.append(child)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    @staticmethod
    def validate_node(candidate):
        Validations.assert_is_updatable(candidate)
        if not isinstance(candidate, SceneGraphNode):
            raise Exception('Graph node must inherit from SceneGraphNode')


class SceneGraph(UpdatableAbc):

    def __init__(self, root_node):
        SceneGraphNode.validate_node(root_node)

        self._root_node = root_node

    def update(self, context):
        self._root_node.update(context)
