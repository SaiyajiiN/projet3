import pygame

from macgyver.graphic.images import load_image
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


class GuardianSprite(pygame.sprite.Sprite):
    """
        Détermine la position du gardien dans
        le labyrinthe et charge une image du gardien.
    """

    def __init__(self, guardian):
        """Chargez l'image du gardien."""
        super().__init__()
        self.image, self.rect = load_image("Gardien.png")
        self.guardian = guardian
        self.update()

    def update(self):
        """Détermine la position de l'image."""
        self.rect.x = (
            self.guardian.position[1] * SPRITE_WIDTH
        )  # postion horizontale depuis le coin gauche de la fenêtre (pixels)
        self.rect.y = (
            self.guardian.position[0] * SPRITE_HEIGHT
        )  # postion verticale depuis le haut de la fenêtre (pixels)
