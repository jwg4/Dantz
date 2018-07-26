from fringe_search import points_set


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
