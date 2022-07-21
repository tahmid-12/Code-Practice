from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
            left, right = 1, n
            res = 0
            
            while left<=right:
                pivot = (left + right) // 2
                coins = (pivot / 2) * (pivot + 1)
                if coins > n:
                    right = pivot - 1
                else:
                    left = pivot + 1
                    res = max(pivot, res)
            return res
        
        
        
        
        
S = Solution()
print(S.arrangeCoins(5))