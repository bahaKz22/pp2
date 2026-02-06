import copy
matrix = [[1, 2], [3, 4]]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0][0] = 100
print(matrix)        # [[1, 2], [3, 4]] → түпнұсқа өзгермеген
print(matrix_copy)   # [[100, 2], [3, 4]]
