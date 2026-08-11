import numpy as np

def fillMatrix(matrix, M, N):

    k = M
        
    for j in range(N):
        ijElement = k
        
        for i in range(M):
            matrix[i, j] = ijElement

            ijElement -= 1

        k += 1 

    return matrix


M = 7
N = 9

matrix = np.zeros((M, N))

matrix = fillMatrix(matrix, M, N)

print(matrix)
