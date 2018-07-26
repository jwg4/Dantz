from dantz_search import build_search_input
from dantz_search import build_search_input_w_gaps
from dantz_search import t_tetromino_tiling
from fringe_search import points_set


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


def test_build_search_input_w_gaps():
    points = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (2, 0)
    ]
    vectors = [
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (1, 0), (1, 1), (2, 0)]
    ]
    names, rows = build_search_input_w_gaps(vectors, points, 2)
    expected_names = [
        "(0, 0)", "(0, 1)", "(0, 2)",
        "(1, 0)", "(1, 1)", "(2, 0)"
    ]
    assert names == expected_names
    expected_rows = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
    ]
    assert rows == expected_rows

def test_t_tetromino_tiling():
    START_X = [0] * 5 + [1] + [0] * 7
    END_X = [12, 11, 12, 11, 13, 13, 13, 13, 13, 14, 13, 14, 13]
    points = points_set(START_X, END_X)
    result = t_tetromino_tiling(points)
    assert len(result) == 10
