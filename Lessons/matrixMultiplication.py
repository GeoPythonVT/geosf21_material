# naive implementation
def matrixMultiplication(A, B):
    """
    Do not use this one because it is too slow.
    """
    assert A.shape[1] == B.shape[0]
    numRow, numCol = A.shape[0], B.shape[1]
    commonDim = A.shape[1] # B.shape[0]
    
    C = np.zeros((numRow, numCol))
    for i in range(numRow):
        for j in range(numCol):
            for k in range(commonDim):
                C[i][j] += A[i][k] * B[k][j]
    return C

#%%        
A = np.array([
              [1, 2],
              [3, 4],
              [5, 6]])
B = np.array([
              [11, 12],
              [13, 14]
             ])

