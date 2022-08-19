from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        res = float("inf")
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(i - left + 1, res)
                total -= nums[left]
                left += 1
        return 0 if res == float("inf") else res
        
        
S = Solution()
print(S.minSubArrayLen([2,3,1,2,4,3],7))