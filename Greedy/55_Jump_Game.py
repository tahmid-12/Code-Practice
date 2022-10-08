from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False
        
        
        
S = Solution()
# print(S.canJump([3,2,1,0,4]))
print(S.canJump([2,3,1,1,4]))
        