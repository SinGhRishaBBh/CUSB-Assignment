#Python program to implement matrix addition
def matrix_addition(matrix1, matrix2):
   

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    #  matrix addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

matrix1 = [
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 7, 1]
]

result = matrix_addition(matrix1, matrix2)

for row in result:
    print(row)

