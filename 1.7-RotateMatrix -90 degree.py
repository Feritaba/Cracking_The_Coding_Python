def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        return False

    for layer in range(len(matrix) // 2):

        length = len(matrix)
        i, j = layer, length - layer - 1

        for index in range(j - i):
            # save top-left
            temp = matrix[i][i + index]

            # top-left = bottom-left
            matrix[i][i + index] = matrix[i + index][j]

            # bottom-left = bottom-right
            matrix[i + index][j] = matrix[j][j - index]

            # bottom-right = top-right
            matrix[j][j - index] = matrix[j - index][i]

            # top-right = top-left
            matrix[j - index][i] = temp

    return matrix


matrix = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

# Test
print(rotate_matrix(matrix))