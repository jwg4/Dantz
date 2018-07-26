ORIENTATIONS = [0, 1, 2, 3]


def orient_t(orientation, point):
    x, y = point
    if orientation == 0:
        return [(x, y+1), (x, y), (x+1, y), (x, y-1)]
    elif orientation == 1:
        return [(x-1, y), (x, y), (x, y+1), (x+1, y)]
    elif orientation == 2:
        return [(x, y+1), (x, y), (x-1, y), (x, y-1)]
    elif orientation == 3:
        return [(x-1, y), (x, y), (x, y-1), (x+1, y)]


def t_search_vectors(points):
    for p in points:
        for o in ORIENTATIONS:
            tetromino = orient_t(o, p)
            if all(p_ in points for p_ in tetromino):
                yield tetromino
