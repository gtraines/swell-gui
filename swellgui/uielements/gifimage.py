from ..utils.gif_image import GIFImage
from .elementbase import ElementBase

class LcarsGifImage(ElementBase):
    
    def __init__(self, imagefilename, pos, ui_config, duration=-1):
        self.image = GIFImage(imagefilename, duration)
        self.pos = pos
        size = (self.image.get_rect().width, self.image.get_rect().height)
        ElementBase.__init__(self, None, pos, size, ui_config)
        
    def update(self, screen):
        if self.visible:
            self.image.render(screen, self.rect)
