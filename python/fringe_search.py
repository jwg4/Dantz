from dantz_search import t_tetromino_tiling


WIDTH = 9
HEIGHT = 11
START_X = [0] * HEIGHT
END_X = [WIDTH] * HEIGHT


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    


if __name__ == '__main__':
    points = points_set(START_X, END_X)
    result = t_tetromino_tiling(points, n_gaps=5)
    print(result)
