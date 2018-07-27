from dantz_search import t_tetromino_tiling


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


if __name__ == '__main__':
    for N in range(0, 10):
        FLAT_END = [4 * N + 2] * 13
        points = points_set(START_X, FLAT_END)
        result = t_tetromino_tiling(points, n_gaps=1)
        print(N, result)
