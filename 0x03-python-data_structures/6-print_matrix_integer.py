#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in rows:
            print("{}".format(column),
                  end="\n"if column == rows[len(rows) - 1] else " ")
