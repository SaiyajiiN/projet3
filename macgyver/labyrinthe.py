import random
from macgyver import hero
from macgyver import guardian
from macgyver import items
from macgyver import directions
from macgyver import constants


class Labyrinthe:
    def __init__(self):
        self.paths = []
        self.walls = []
        self.hero = None
        self.guardian = None
        self.width = 0
        self.height = 0
        self.items = []

    def read_file(self):
        with open('labyrinthe.txt', 'r') as file:
            for position_ligne, ligne in enumerate(file):
                for position, character in enumerate(ligne):
                    if character == "D":
                        self.macgyver = hero.Hero(
                            (position_ligne, position), self
                        )
                        self.start = (position_ligne, position)
                        self.paths.append((position_ligne, position))
                    elif character == ".":
                        self.paths.append((position_ligne, position))
                    elif character == "#":
                        self.walls.append((position_ligne, position))
                    elif character == "A":
                        self.guardian = guardian.Guardian(
                            (position_ligne, position), self
                        )
                        self.paths.append((position_ligne, position))
        self.width = position + 1
        self.height = position_ligne + 1

        for i, position in enumerate(
            random.sample(
                set(self.paths)
                - {self.macgyver.position, self.guardian.position},
                len(constants.NAME_ITEMS),
            )
        ):
            self.items.append(
                items.Item(self, position, constants.NAME_ITEMS[i])
            )
