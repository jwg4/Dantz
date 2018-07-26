from fringe_search import points_set, t_search_vectors
from fringe_search import build_search_input, orient_t
from fringe_search import t_tetromino_tiling


def test_orient_t():
    p = (2, 0)
    assert set(orient_t(1, p)) == set([(1, 0), (2, 0), (3, 0), (2, 1)])


def test_points_set():
    starts = [0, 1, 0]
    ends = [3, 4, 5]
    expected = set(
        [
            (0, 0), (1, 0), (2, 0),
            (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)
        ]
    )
    assert points_set(starts, ends) == expected


def test_t_search_vectors():
    points = [
        (0, 0), (1, 0), (2, 0),
        (0, 1), (1, 1), (2, 1),
        (0, 2), (1, 2), (2, 2),
    ]
    vectors = list(t_search_vectors(points))
    assert len(vectors) == 8


def test_t_search_vectors():
    points = [
        (7, 3), (6, 9), (11, 11), (7, 12), (12, 12), (0, 7), (1, 6),
        (0, 10), (3, 7), (2, 5), (1, 11), (8, 5), (5, 8), (4, 0),
        (10, 8), (9, 0), (6, 7), (5, 5), (11, 5), (10, 7), (7, 6),
        (6, 10), (12, 6), (0, 4), (1, 1), (4, 10), (3, 2), (2, 6),
        (8, 2), (5, 11), (4, 5), (9, 3), (6, 0), (11, 0), (7, 5),
        (12, 11), (0, 1), (3, 12), (1, 12), (8, 12), (3, 1), (2, 11),
        (9, 9), (7, 8), (12, 8), (3, 11), (2, 1), (8, 9), (4, 12),
        (2, 12), (9, 4), (5, 1), (10, 3), (7, 2), (11, 10), (1, 5),
        (0, 11), (3, 6), (2, 2), (1, 10), (8, 6), (4, 1), (10, 9),
        (9, 7), (6, 4), (5, 4), (11, 4), (10, 4), (7, 1), (6, 11),
        (12, 7), (11, 9), (0, 5), (1, 0), (0, 8), (4, 11), (3, 5),
        (2, 7), (8, 3), (5, 10), (4, 6), (10, 10), (9, 2), (6, 1),
        (5, 7), (7, 4), (12, 4), (13, 9), (0, 2), (1, 3), (4, 8),
        (3, 0), (2, 8), (9, 8), (8, 0), (6, 2), (7, 11), (12, 9),
        (3, 10), (8, 10), (9, 11), (5, 0), (10, 0), (1, 4), (0, 12),
        (3, 9), (2, 3), (1, 9), (8, 7), (4, 2), (9, 6), (6, 5), (5, 3),
        (11, 7), (10, 5), (7, 0), (6, 8), (11, 8), (0, 6), (1, 7),
        (0, 9), (3, 4), (2, 4), (9, 12), (8, 4), (5, 9), (4, 7),
        (10, 11), (9, 1), (6, 6), (5, 6), (11, 2), (10, 6), (7, 7),
        (12, 5), (0, 3), (1, 2), (4, 9), (3, 3), (2, 9), (8, 1),
        (5, 12), (4, 4), (10, 12), (6, 3), (7, 10), (12, 10), (13, 11),
        (8, 11), (2, 10), (9, 10), (10, 1), (6, 12), (11, 12), (7, 9),
        (3, 8), (2, 0), (1, 8), (8, 8), (4, 3), (9, 5), (5, 2), (11, 6),
        (10, 2)
    ]
    vectors = list(t_search_vectors(points))
    v = [(1, 0), (2, 0), (2, 1), (3, 0)]
    assert v in vectors


def test_build_search_input():
    vectors = [
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (1, 0), (1, 1), (2, 0)]
    ]
    names, rows = build_search_input(vectors)
    expected_names = [
        "(0, 0)", "(0, 1)", "(0, 2)",
        "(1, 0)", "(1, 1)", "(2, 0)"
    ]
    assert names == expected_names
    expected_rows = [
        [1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 1]
    ]
    assert rows == expected_rows


def test_build_search_input_with_gtor():
    vector_list = [
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (1, 0), (1, 1), (2, 0)]
    ]
    vectors = ( v for v in vector_list )
    names, rows = build_search_input(vectors)
    expected_rows = [
        [1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 1]
    ]
    assert rows == expected_rows

def test_t_tetromino_tiling():
    START_X = [0] * 5 + [1] + [0] * 7
    END_X = [12, 11, 12, 11, 13, 13, 13, 13, 13, 14, 13, 14, 13]
    points = points_set(START_X, END_X)
    result = t_tetromino_tiling(points)
    assert len(result) == 41
