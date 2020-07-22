import os
import pygame

from pygame.compat import geterror
from macgyver.constants import SPRITE_WIDTH, SPRITE_HEIGHT


def load_image(name, colorkey=None):
    # fonctions pour créer nos ressources
    """Méthode pour charger une image."""
    fullname = os.path.join("ressource", name)
    try:
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (SPRITE_WIDTH, SPRITE_HEIGHT))
    except pygame.error:
        print("Impossible de charger l'image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()
