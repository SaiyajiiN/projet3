from macgyver.labyrinthe import labyrinthe
from macgyver.directions import right, left, up, down
from macgyver.text.display import LabyrintheDisplay


def main():
    labyrinthe = Labyrinthe()
    labyrinthe.load_structure()
    display = LabyrintheDisplay(labyrinthe)
    running = True
    while running:
        print(display)
        response = input("Que voulez-vous faire: (q,r,l,u,d) ")
        if response == "q":
            running = False
        elif response == "r":
            running = labyrinthe.macgyver.move(right)
        elif response == "l":
            running = labyrinthe.macgyver.move(left)
        elif response == "u":
            running = labyrinthe.macgyver.move(up)
        elif response == "d":
            running = labyrinthe.macgyver.move(down)

    if labyrinthe.macgyver.status == "win":
        print("Victoire")
    else:
        print("Defaite")


if __name__ == "__main__":
    main()
