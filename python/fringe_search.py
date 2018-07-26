START_X = [1] + [0] * 12
END_X = [12, 11, 12, 11, 13, 13, 13, 13, 13, 14, 13, 14, 13]


def generate_points(starts, ends):
    for y in range(0, len(starts)):
        for x in range(starts[y], ends[y]):
            yield (x, y)


def points_set(starts, ends):
    return set(generate_points(starts, ends))    
