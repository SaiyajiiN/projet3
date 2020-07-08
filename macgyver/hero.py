from macgyver import constants


class Hero:
    def __init__(self, position, labyrinthe):
        self.labyrinthe = labyrinthe
        self.position = position
        self.count_items = []
        self.status = None

    def move(self, direction):
        """Créez la position de départ du héros et les positions après le mouvement."""
        position = direction(position=self.position)
        if position in self.labyrinthe.paths:
            self.position = position
            for i, item in enumerate(self.labyrinthe.items):
                if position == item.position:
                    self.catch_item(i, item)
            if position == self.labyrinthe.guardian.position:
                self.goal()
                return False
        return True

    def catch_item(self, index, item):
        """Déplacer des objets après les avoir récupérés."""
        item.status = "catched"
        self.count_items.append(item)
        del self.labyrinthe.items[index]

    def goal(self):
        if len(self.count_items) == len(constants.NAME_ITEMS):
            self.status = "won"
        else:
            self.status = "lost"
