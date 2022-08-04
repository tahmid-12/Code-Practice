from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result,nums[left])
                break
                
            pivot = (left + right) // 2
            result = min(result, nums[pivot])
            if nums[pivot] >= nums[left]:
                left = pivot + 1
            else:
                right = pivot - 1
        return result


S = Solution()
print(S.findMin([4,5,6,7,0,1,2]))