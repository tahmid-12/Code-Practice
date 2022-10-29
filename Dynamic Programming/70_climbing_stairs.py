from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        else:
            one, two = 1, 1
            
            for i in range(n -1):
                temp = one
                one = one + two
                two = temp
            
            return one
        
        

S = Solution()
print(S.climbStairs(3))