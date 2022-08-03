from typing import List

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # return c
        left = 0
        right = int(c/2)
        
        while left <= right:
            result = left * left + right * right
            if result < c:
                left += 1
            elif result > c:
                right -= 1
            else:
                return True
        return False
        
        
        
        

S = Solution()
print(S.judgeSquareSum(5))