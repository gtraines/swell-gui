import pygame
from .elementcontainer import Dimensions2D, ElementContainerAbc,
                    RelativeDimensions,
                    RelativeElementAbc,
                    RelativeElementDescription,
                    RelativeOffsetCoord


class UiRect(RelativeElementAbc):
    
    def __init__(self, top_left_offset, relative_dimensions, style=None):
        """
            dimensions - Dimensions2D
        """
        rel_desc = RelativeElementDescription(top_left_offset=top_left_offset,
                                          relative_dimensions=relative_dimensions,
                                          relative_layer=1)
        RelativeElementAbc.__init__(self, rel_desc)
    
    def draw_element(self, top_left_corner_coords, absolute_dimensions, layer):
        """ Implement from abstract base """
        self._screen.fill(ColorConsts.BLUE)


class UiScreen(UiRect):
    def __init__(self):
        top_left_offset = RelativeOffsetCoord(x_percent_offset=0, y_percent_offset=0)
        dims = RelativeDimensions(height_percent=100, width_percent=100)
        UiRec.__init__(self, top_left_offset, dims)


class UiContainer(ElementContainerAbc):
    """
    Sample UI container
    """
    def __init__(self, ui_config):
        """ args == element, element_parent, *children """
        self._config = ui_config
        relative_dimensions = RelativeDimensions(height_percent=100, width_percent=100)
        element = UiScreen()
        RelativeElementAbc.__init__(self, )


class ScalableScreen:
    
    def __init__(self, starting_dimensions, background_image_filename=None):
        if background_image_filename is not None:
            self.background_image_original = pygame.image.load(
                background_image_filename
            )
        
        self.background_image = pygame.transform.scale(
            self.background_image_original,
            (starting_dimensions.width, starting_dimensions.height))