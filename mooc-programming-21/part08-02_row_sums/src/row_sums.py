def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))