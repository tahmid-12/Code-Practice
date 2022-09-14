from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for index in range(1, len(nums)):
            if nums[index - 1] > 0:
                nums[index] += nums[index - 1]
        return max(nums)
        
        
S = Solution()
print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))