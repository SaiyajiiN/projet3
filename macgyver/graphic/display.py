import os, pygame


def __str__(self):
    """Retourne le texte du labyrinthe pour afficher avec print."""
    laby = ""
    needle, tube, ether = self.labyrinthe.item_positions
    for x in range(self.labyrinthe.height):
        for y in range(self.labyrinthe.width):
            if (x, y) == self.labyrinthe.macgyver.position:
                laby += "M"
            elif (x, y) == self.labyrinthe.guardian.position:
                laby += "G"
            elif (x, y) == needle and (x, y) not in self.labyrinthe.macgyver.catch_items:
                laby += "N"
            elif (x, y) == tube and (x, y) not in self.labyrinthe.macgyver.catch_items:
                laby += "T"
            elif (x, y) == ether and (x, y) not in self.labyrinthe.macgyver.catch_items:
                laby += "E"
            elif (x, y) in self.labyrinthe.paths:
                laby += "."
            else:
                laby += "#"
        laby += "\n"

    return laby
