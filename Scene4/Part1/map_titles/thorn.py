from Scene4.game_object4_1 import GameObject
from Scene4.renderer.image_redenrer import ImageRenderer
from Scene4.box_collider import BoxCollider
import pygame

class Thorn(GameObject):
    def __init__(self,x , y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer('Scene4/images/trap/thorn.png')
        # self.image = pygame.image.load('../images/trap/thorn.png')
        self.collider = BoxCollider(24, 30)

