from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
S = Solution()
print(S.rob([1,3,1]))