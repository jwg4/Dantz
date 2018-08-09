from dantz_search import t_tetromino_tiling


START_X = [0] * 13
_END_X = [4, 3, 4, 3, 5, 5, 5, 5, 5, 6, 5, 6, 5]
_REV_ENDS = [ 8 - x for x in _END_X ]


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    


if __name__ == '__main__':
    for N in range(0, 100):
        END_X = [ e + N for e in _REV_ENDS ]
        points = points_set(START_X, END_X)
        result = t_tetromino_tiling(points, n_gaps=1)
        print(N, result)
