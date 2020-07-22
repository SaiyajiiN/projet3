import random
from macgyver import hero
from macgyver import guardian
from macgyver import items
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
        # ouvrir le fichier labyrinthe.txt en tant que fichier
        with open('labyrinthe.txt', 'r') as file:
            # POUR chaque numéro_ligne et ligne dans fichier FAIRE
            for position_ligne, ligne in enumerate(file):
                # POUR chaque numéro_caractère et caractère DANS ligne FAIRE
                for position, character in enumerate(ligne.strip()):
                    # SI caractère est "D" FAIRE
                    if character == "D":
                        # self.hero <- (0, numéro_caractère)
                        self.macgyver = hero.Hero(
                            (position_ligne, position), self
                        )
                        self.start = (position_ligne, position)
                        self.paths.append((position_ligne, position))
                        # SINON SI caractère est "." FAIRE
                    elif character == ".":
                        # Ajouter (0, numéro_caractère) à la liste self.paths
                        self.paths.append((position_ligne, position))
                        # SINON SI caractère est "#" FAIRE
                    elif character == "#":
                        # Ajouter (0, numéro_caractère) à la liste self.walls
                        self.walls.append((position_ligne, position))
                        # SINON SI caractère est "A" FAIRE
                    elif character == "A":
                        # self.guardian <- (position_ligne, numéro_caractère)
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
