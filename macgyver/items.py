class Item:
    def __init__(self, labyrinthe, position, name):
        self.status = "not catched"
        self.position = position
        self.name = name
        self.labyrinthe = labyrinthe
