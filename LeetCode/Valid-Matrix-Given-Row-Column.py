"""
Given a matrix of Rows/Columsn find the  matrix that sums up to each one
ex: 
6 6 0 0
7 2 3 2
8 0 0 3
  8 3 5
"""


def findMatrix(rowSum: list[int], colSum: list[int]) -> list[int]:
    rows = len(rowSum)
    cols = len(colSum)
        # Blank matrix with all 0
    matrix = [[0 for x in range(rows)]for y in range(cols)]
    print(matrix)

    for i in range(rows):
        for j in range(cols):
            m = min(rowSum[i], colSum[j])
            print(matrix)
            if m > 0:
                matrix[i][j] = m
                colSum[j] -= m
                rowSum[i] -= m
            else: # Adding zero to Matrix/ could not since they are all zeros anyway
                matrix[i][j] == m
    return matrix
 


# 8 6 2 0 
# 3 0 3 0
# 5 0 2 3
#  6 7 8

print(findMatrix([8,3,5, 6], [6,7,8, 7]))
