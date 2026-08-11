import numpy as np

def fillMatrix2(matrix, N):

    k = N
        
    for j in range(N):
        ijElement = k
        
        for i in range(N):
            matrix[i, j] = ijElement

            if i >= j:
                ijElement -= 1
            else:
                ijElement += 1

        k -= 1 

    return matrix


N = 4

matrix = np.zeros((N, N))

matrix = fillMatrix2(matrix, N)

print(matrix)