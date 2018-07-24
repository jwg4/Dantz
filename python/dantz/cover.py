from ctypes import c_int, c_char_p, c_int_p, cdll


def exact_cover(rows, names):
    c_width = c_int(len(rows[0]))
    c_count = c_int(len(rows))

    c_names = c_char_p('') * c_count
    c_rows = c_int_p('') * c_count

    for i in range(0, c_count):
        c_s = c_char_p(names[i])
        c_names[i] = c_s

        c_row = c_int(0) * c_width
        for j in range(0, c_width):
            c_row[j] = rows[i][j]

        c_rows[i] = c_row 

    c_dantz = cdll.LoadLibrary("dantz.so")
    result = c_dantz.solve_exact_cover(c_rows, c_names, c_width, c_count)
    return result
