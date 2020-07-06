def up(position):
    y, x = position
    return (y - 1, x)


def down(position):
    y, x = position
    return (y + 1, x)


def right(position):
    y, x = position
    return (y, x + 1)


def left(position):
    y, x = position
    return (y, x - 1)
