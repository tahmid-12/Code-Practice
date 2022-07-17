from typing import List

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left < right:
            pivot = (left + right)//2
            if pivot*pivot >= num:
                right = pivot
            else:
                left = pivot + 1
        return left**2 == num
        
        
S = Solution()
# list = [0,10,5,2]
print(S.isPerfectSquare(168))