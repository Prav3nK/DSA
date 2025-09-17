# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        # Flatten the matrix into a list
        flat_list = []
        for i in range(m):
            for j in range(n):
                flat_list.append(mat[i][j])
        
        # Reshape the flat list into r x c matrix
        reshaped = []
        index = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat_list[index])
                index += 1
            reshaped.append(row)
        
        return reshaped