
import os
import sys

import pygame

from macgyver.labyrinthe import Labyrinthe
from macgyver.directions import right, left, up, down
from macgyver.graph.labyrinthe import LabyrintheDisplay
from macgyver.graph.hero import HeroSprite
from macgyver.graph.items import ItemSprite
from macgyver.graph.guardian import GuardianSprite
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


if not pygame.font: print('Attention, polices désactivées')
if not pygame.mixer: print('Attention, son désactivé')


class Game:
    """Créez la fenêtre de jeu et ajoutez le héros, les objets et le gardien."""
    def __init__(self):
        pygame.init()

        self.labyrinthe = Labyrinthe()
        self.labyrinthe.read_file()
        self.screen = pygame.display.set_mode((SPRITE_WIDTH * self.labyrinthe.width, SPRITE_HEIGHT * (self.labyrinthe.height + 1)))
        self.screen.fill((0, 0, 0))
        self.background = LabyrintheDisplay(self.labyrinthe)
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(HeroSprite(self.labyrinthe.macgyver))
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
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        running = self.labyrinthe.macgyver.move(left)
                    elif event.key == pygame.K_RIGHT:
                        running = self.labyrinthe.macgyver.move(right)
                    elif event.key == pygame.K_UP:
                        running = self.labyrinthe.macgyver.move(up)
                    elif event.key == pygame.K_DOWN:
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
            self.screen.blit(pygame.image.load(image), (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
