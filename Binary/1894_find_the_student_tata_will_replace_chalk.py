from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        N = len(chalk)
        
        if total % k == 0:
            return 0
            
        left = k % total
        for index in range(N):
            left -= chalk[index]
            if left < 0:
                return index
        
        
        
S = Solution()
print(S.chalkReplacer([5,1,5],22))