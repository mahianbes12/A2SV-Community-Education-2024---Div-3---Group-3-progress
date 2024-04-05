from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                    
        return True

def test():
    sol = Solution()
    matrix1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    matrix2 = [[1,2],[2,2]]

    assert sol.isToeplitzMatrix(matrix1) == True
    assert sol.isToeplitzMatrix(matrix2) == False

test()