from dantz import exact_cover


def test_basic_example():
    data = [
        [ 0, 0, 1, 0, 1, 1, 0 ],
        [ 1, 0, 0, 1, 0, 0, 1 ],
        [ 0, 1, 1, 0, 0, 1, 0 ],
        [ 1, 0, 0, 1, 0, 0, 0 ],
        [ 0, 1, 0, 0, 0, 0, 1 ],
        [ 0, 0, 0, 1, 1, 0, 1 ],
    ]
    assert exact_cover(data) = [0, 3, 4]
