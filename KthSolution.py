from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
        
        
S = Solution()
nums, n = [3,2,1,5,6,4], 2
print(S.findKthLargest(nums,n))
