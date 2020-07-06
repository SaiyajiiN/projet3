import pygame

from macgyver.graphic.images import load_image
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


class ItemSprite(pygame.sprite.Sprite):
    def __init__(self, item):
        """Chargez les images de tous les éléments dans le labyrinthe."""
        super().__init__()
        self.image, self.rect = load_image(f"{item.name}.png", -1)
        self.item = item
        self.update()

    def update(self):
        """Détermine les positions des images."""
        if self.item.status == "not catched":
            self.rect.x = (
                self.item.position[1] * SPRITE_WIDTH
            )  # postion horizontale depuis le coin gauche de la fenêtre (pixels)
            self.rect.y = (
                self.item.position[0] * SPRITE_HEIGHT
            )  # postion verticale depuis le haut de la fenêtre (pixels)
        else:
            self.rect.x = -1 * SPRITE_WIDTH
            self.rect.y = -1 * SPRITE_HEIGHT
