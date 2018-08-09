from dantz_search import t_tetromino_tiling


START_X = [0] * 13
_END_X = [4, 3, 4, 3, 5, 5, 5, 5, 5, 6, 5, 6, 5]


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    


if __name__ == '__main__':
    for N in range(3, 10):
        END_X = [ e + N * 4 for e in _END_X ]
        points = points_set(START_X, END_X)
        flipped = set( (x[1], x[0]) for x in points )
        corner_points = points.union(flipped)
        result = t_tetromino_tiling(corner_points, n_gaps=3)
        print(N, result)
