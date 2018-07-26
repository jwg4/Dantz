START_X = [1] + [0] * 12
END_X = [12, 11, 12, 11, 13, 13, 13, 13, 13, 14, 13, 14, 13]


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    


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


def build_search_input(vectors):
    points = sorted(list(set([ p for v in vectors for p in v ])))
    names = [ str(p) for p in points ]
    rows = [
        [ (1 if p in v else 0) for p in points ]
        for v in vectors 
    ]
    return names, rows 
    
