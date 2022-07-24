from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        found = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == target):
                    found = True
        return found
        
        
        
        
S = Solution();
print(S.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],58))