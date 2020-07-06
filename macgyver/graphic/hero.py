import pygame

from macgyver.graphic.images import load_image
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, hero):
        """Chargez l'image du Hero."""
        super().__init__()
        self.image, self.rect = load_image("MacGyver.png", -1)
        self.hero = hero
        self.update()

    def update(self):
        """Détermine la position de l'image."""
        self.rect.x = (
            self.hero.position[1] * SPRITE_WIDTH
        )  # postion horizontale depuis le coin gauche de la fenêtre (pixels)
        self.rect.y = (
            self.hero.position[0] * SPRITE_HEIGHT
        )  # postion verticale depuis le haut de la fenêtre (pixels)
