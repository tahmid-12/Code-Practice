from typing import List

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 0
        higher = n
        
        while lower <= higher:
            
            mid = (lower + higher) // 2
            pick = guess(mid)
            
            if pick == 0:
                return mid
            elif pick == 1:
                lower = mid + 1
            else:
                higher = mid - 1
