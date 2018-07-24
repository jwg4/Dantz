import os

from ctypes import c_int, c_char_p, c_void_p, cdll, POINTER


def exact_cover(rows, names):
    width = len(rows[0])
    c_width = c_int(width)
    
    count = len(rows)
    c_count = c_int(count)

    c_names = (c_char_p * count)()
    c_rows = (POINTER(c_int) * count)()

    for i in range(0, count):
        c_s = c_char_p(names[i])
        c_names[i] = c_s

        c_row = (c_int * width)()
        for j in range(0, width):
            c_row[j] = rows[i][j]

        c_rows[i] = c_row 

    c_dantz = cdll.LoadLibrary(os.path.abspath("dantz.so"))
    result = c_dantz.solve_exact_cover(c_rows, c_names, c_width, c_count)
    return result
