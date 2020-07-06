import pygame

from macgyver.graphic.images import load_image
from macgyver.constants import SPRITE_WIDTH, SPRITE_HEIGHT


class LabyrintheDisplay(pygame.Surface):
    """Dessinez les murs du labyrinthe et chargez les images des murs."""

    def __init__(self, labyrinthe):
        self.labyrinthe = labyrinthe
        super().__init__(
            (
                self.labyrinthe.width * SPRITE_WIDTH,
                self.labyrinthe.height * SPRITE_HEIGHT,
            )
        )
        self.wall, self.wall_rect = load_image("mur.png")
        self.fill((255, 255, 255))
        for y, x in self.labyrinthe.walls:
            self.blit(self.wall, (x * SPRITE_WIDTH, y * SPRITE_HEIGHT))
