import pygame
from .shapenodes import RectangleElement
from .media import GifImage


class GifImageElement(RectangleElement):
    
    def __init__(self, imagefilename, pos, ui_config, duration=-1):
        self.image = GifImage(imagefilename, duration)
        self.pos = pos
        size = (self.image.get_rect().width, self.image.get_rect().height)
        RectangleElement.__init__(self, None, pos, size, ui_config)
        
    def update(self, screen):
        if self.visible:
            self.image.render(screen, self.rect)


class ImageElement(RectangleElement):
    def __init__(self, image, pos, ui_config):
        self.image = pygame.image.load(image).convert()
        RectangleElement.__init__(self, None, pos, None, ui_config)


class BackgroundImageElement(ImageElement):
    def __init__(self, image, ui_config):
        self.image = pygame.image.load(image).convert()
        RectangleElement.__init__(self, None, (0, 0), None, ui_config)

    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False
