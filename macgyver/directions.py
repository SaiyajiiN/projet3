def up(position):
    x, y = position
    return (x, y-1)

def down(position):
    x, y = position
    return (x, y+1)

def right(position):
    x, y = position
    return (x+1, y)

def left(position):
    x, y = position
    return (x-1, y)
