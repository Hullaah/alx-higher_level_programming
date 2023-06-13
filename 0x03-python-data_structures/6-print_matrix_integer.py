#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        if not rows:
            print()
        for column in rows:
            print("{:d}".format(column),
                  end="\n"if column == rows[len(rows) - 1] else " ")
