from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] < nums[right]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right = right - 1
            
        return nums[left]
        

S = Solution()
print(S.findMin([6,3,2]))
                