from dantz_search import t_tetromino_tiling


START_X = [0] * 13
_END_X = [4, 3, 4, 3, 5, 5, 5, 5, 5, 6, 5, 6, 5]


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    


def points_to_skip(n):
    for i in range(0, n):
        for j in range(0, 2):
            x = 4 * i + j
            yield (x, 0)
            yield (x, 12)


if __name__ == '__main__':
    for N in range(2, 10):
        END_X = [ e + N * 4 for e in _END_X ]
        for skip in points_to_skip(N + 1):
            points = points_set(START_X, END_X)
            points.remove(skip)
            result = t_tetromino_tiling(points, n_gaps=0)
            print(N, skip, result)
