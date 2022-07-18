from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0,  x
        while left <= right:
            pivot = left + (right - left) // 2

            if pivot * pivot > x:
                right = pivot - 1
            elif pivot * pivot < x:
                left = pivot + 1
            else:
                return pivot

        return right
        
        
        

S = Solution()
print(S.mySqrt(18))