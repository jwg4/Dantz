from dantz import exact_cover
from tetromino import t_search_vectors


def build_search_input(vectors):
    vectors = list(vectors)
    points = sorted(list(set([ p for v in vectors for p in v ])))
    names = [ str(p) for p in points ]
    rows = [
        [ (1 if p in v else 0) for p in points ]
        for v in vectors 
    ]
    return names, rows 


def build_search_input_w_gaps(vectors, points, n_gaps):
    vectors = list(vectors)
    names = [ str(p) for p in points ]
    rows = [
        [ (1 if p in v else 0) for p in points ] + [0] * n_gaps
        for v in vectors 
    ]

    np = len(points)
    n = n_gaps + np
    for g in range(0, n_gaps):
        names.append("mono_%d" % (g, ))
        for p in range(0, np):
            row = [0] * n
            row[p] = 1
            row[np + g] = 1
            rows.append(row)
    return names, rows 


def t_tetromino_tiling(points, n_gaps=0):
    vectors = t_search_vectors(points)

    if n_gaps:
        names, rows = build_search_input_w_gaps(vectors, points, n_gaps)
    else:
        names, rows = build_search_input(vectors)
    result = exact_cover(rows, names)
    return result
