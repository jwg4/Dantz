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
    names = ["0", "1", "2", "3", "4", "5", "6"]
    expected = [['2', '4', '5'], ['0', '3'], ['1', '6']]
    assert sorted(exact_cover(data, names)) == sorted(expected)
