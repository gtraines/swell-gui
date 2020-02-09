from abc import abstractmethod
import pygame
from collections import namedtuple
from ..abscore import UpdatableAbc

RelativeOffsetCoord = namedtuple('RelativeOffsetCoord', 
                                ['x_percent_offset', 'y_percent_offset'])

RelativeDimensions = namedtuple('RelativeDimensions',
                                ['height_percent', 'width_percent'])

ScalingCoefficentVector2D = namedtuple('ScalingCoefficientVector2D',
                                        ['x_coefficient', 'y_coefficient'])

Coord2D = namedtuple('Coord2D', ['x', 'y'])

Dimensions2D = namedtuple('Dimensions2D', 
        ['height', 'width']
    )

RelativeElementDescription = namedtuple('RelativeElementDescription', [
    'topleft_offset',
    'relative_dimensions',
    'relative_layer'
])


class RelativeElementAbc:
    
    def __init__(self, relative_description):
        """
        relative_description: RelativeElementDescription
        """
        self._relative_element_description = relative_description
        self.absolute_element = None
        
    @property
    def relative_element_description(self):
        return self._relative_element_description
    
    @property
    def relative_offset_coords(self):
        return self.relative_element_description.topleft_offset
    
    @property
    def relative_dimensions(self):
        return self.relative_element_description.relative_dimensions
    
    @property
    def relative_layer(self):
        return self.relative_element_description.relative_layer
    
    def get_absolute_topleft_coords(self, parent_topleft_coord, parent_dimensions):
        x_coord = parent_topleft_coord.x + (
            self.relative_offset_coords.x_percent_offset * parent_dimensions.width)
        y_coord = parent_topleft_coord.y + (
            self.relative_offset_coords.y_percent_offset * parent_dimensions.height)
        
        return Coord2D(x=x_coord, y=y_coord)
    
    def get_absolute_dimensions(self, parent_dimensions):
        height = parent_dimensions.height * self.relative_dimensions.height_percent
        width = parent_dimensions.width * self.relative_dimensions.width_percent

        return Dimensions2D(height=height, width=width)
    
    def get_absolute_layer(self, parent_layer):
        absolute_layer = self.relative_layer + parent_layer
        return absolute_layer

    def draw_absolute(self, parent_topleft_coord, parent_dimensions, parent_layer, context):
        topleft_coords = self.get_absolute_topleft_coords(
            parent_topleft_coord, 
            parent_dimensions)
        absolute_dimensions = self.get_absolute_dimensions(parent_dimensions)
        layer = self.get_absolute_layer(parent_layer)
        
        # DO THE DRAW STUFF
        self.draw_element(topleft_coords, absolute_dimensions, layer, context)
        return True
        
    @abstractmethod
    def draw_element(self, topleft_coords, absolute_dimensions, layer, context):
        pass


class ElementContainerAbc(UpdatableAbc):
    
    def __init__(self, element, element_parent, *children):
        self.validate_element(element)
        self._element = element
        
        if hasattr(element, 'name'):
            self._name = element.name
        else:
            self._name = str(element)
            
        self._element_parent = element_parent
        self._children = []
        
        if children is not None and len(children) > 0:
            for child in children:
                self.add_child(child)
    
    def add_child(self, element_to_add):
        self.validate_element(element_to_add)
        self._children.append(element_to_add)
    
    def update(self, context):
        success = self._element.update(context)
        try:
            for child in self._children:
                update_result = child.update(context)
                if not update_result:
                    raise Exception(child.name)
        
        except Exception as ex:
            raise Exception('Child of element failed to update', ex)
        return success
    
    @abstractmethod
    def set_relative_position(self, context):
        pass
    
    @abstractmethod
    def get_position_relative_to_parent(self, context):
        pass
    
    def draw(self, context):
        topleft_relative_coord = self.get_position_relative_to_parent(context)

    @staticmethod
    def validate_element(element):
        if not isinstance(element, UpdatableAbc):
            raise Exception('Elements must implement UpdatableAbc')
