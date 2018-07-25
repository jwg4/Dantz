import os

from ctypes import c_int, c_char_p, c_void_p, cdll, POINTER, c_bool, py_object


def exact_cover(rows, names):
    width = len(rows[0])
    c_width = c_int(width)
    
    count = len(rows)
    c_count = c_int(count)

    c_names = (c_char_p * width)()
    c_rows = (POINTER(c_bool) * count)()

    for i in range(0, width):
        c_s = c_char_p(names[i])
        c_names[i] = c_s

    for i in range(0, count):
        c_row = (c_bool * width)()
        for j in range(0, width):
            c_row[j] = rows[i][j]

        c_rows[i] = c_row 

    c_dantz = cdll.LoadLibrary(os.path.abspath("src/dantz.so"))
    c_dantz.solve_exact_cover.restype = py_object
    result = c_dantz.solve_exact_cover(c_rows, c_names, c_width, c_count)
    return result
