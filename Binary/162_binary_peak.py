from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        else:
            left = 0
            right = len(nums) - 1

            while left < right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot - 1] and nums[pivot] > nums[pivot + 1]:
                    return pivot
                elif nums[pivot] < nums[pivot - 1]:
                    right = pivot
                elif nums[pivot] < nums[pivot + 1]:
                    left = pivot
        
        
S = Solution()
print(S.findPeakElement([1,2,1,3,5,6,4]))
# print(S.findPeakElement([1,2,3,1]))