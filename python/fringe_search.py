from dantz import exact_cover


START_X = [0] * 12 + [1]
_END_X = [4, 3, 4, 3, 5, 5, 5, 5, 5, 6, 5, 6, 5]
WIDTH = 20
END_X = [ e + WIDTH for e in _END_X ]


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
    vectors = list(vectors)
    points = sorted(list(set([ p for v in vectors for p in v ])))
    names = [ str(p) for p in points ]
    rows = [
        [ (1 if p in v else 0) for p in points ]
        for v in vectors 
    ]
    return names, rows 


def t_tetromino_tiling(points):
    vectors = t_search_vectors(points)
    names, rows = build_search_input(vectors)
    result = exact_cover(rows, names)
    return result


if __name__ == '__main__':
    points = points_set(START_X, END_X)
    result = t_tetromino_tiling(points)
    print(result)
