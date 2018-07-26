from fringe_search import points_set, t_search_vectors, build_search_input


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
    print names
    assert names == expected_names
