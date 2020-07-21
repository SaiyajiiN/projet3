import os
import sys

import pygame

from macgyver.labyrinthe import Labyrinthe
from macgyver.directions import right, left, up, down
from macgyver.graphic.labyrinthe import LabyrintheDisplay
from macgyver.graphic.hero import HeroSprite
from macgyver.graphic.items import ItemSprite
from macgyver.graphic.guardian import GuardianSprite
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


if not pygame.font:
    print('Attention, polices désactivées')
if not pygame.mixer:
    print('Attention, son désactivé')


class Game:
    """Créez la fenêtre de jeu et ajoutez le héros, les objets et le gardien."""

    def __init__(self):
        pygame.init()  # Pygame is initialized

        self.labyrinthe = Labyrinthe()
        self.labyrinthe.read_file()
        self.screen = pygame.display.set_mode(
            (
                SPRITE_WIDTH * self.labyrinthe.width,
                SPRITE_HEIGHT * (self.labyrinthe.height),
            )
        )
        self.screen.fill((0, 0, 0))
        self.background = LabyrintheDisplay(self.labyrinthe)
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(HeroSprite(self.labyrinthe.macgyver, self.screen))
        for item in self.labyrinthe.items:
            self.allsprites.add(ItemSprite(item))
        self.allsprites.add(GuardianSprite(self.labyrinthe.guardian))
        self.clock = pygame.time.Clock()

    def start(self):
        """Lancement du jeu et affectation des touches fléchées du héros."""
        running = True
        while running:
            self.clock.tick(40)
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                # Recherche tous les événements qui se produisent pendant le
                # jeu
                if event.type == pygame.QUIT:
                    running = False
                # La boucle est arrêtée et les fenêtres de jeu sont fermées
                elif event.type == pygame.KEYDOWN:
                    # Touche utilisée pour déplacer MacGyver
                    if event.key == pygame.K_LEFT:
                        # SI vous appuyez sur la flèche de gauche
                        running = self.labyrinthe.macgyver.move(left)
                    elif event.key == pygame.K_RIGHT:
                        # SINON SI vous appuyez sur la flèche de droite
                        running = self.labyrinthe.macgyver.move(right)
                    elif event.key == pygame.K_UP:
                        # SINON SI vous appuyez sur la flèche du haut
                        running = self.labyrinthe.macgyver.move(up)
                    elif event.key == pygame.K_DOWN:
                        # SINON SI vous appuyez sur la flèche du bas
                        running = self.labyrinthe.macgyver.move(down)
            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.update()

        if self.labyrinthe.macgyver.status == "won":
            self.display_victory_or_defeat('ressource/victoire.png')
        else:
            self.display_victory_or_defeat('ressource/defaite.png')

    def display_victory_or_defeat(self, image):
        """Charge une image si le joueur gagne ou perd."""
        running = True
        while running:
            self.clock.tick(20)
            self.screen.blit(pygame.image.load(image), (120, 120))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
