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
    names = ["0", "1", "2", "3", "4", "5"]
    assert exact_cover(data, names) == ["0", "3", "4"]
