from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = (left + right) // 2
            # print(pivot)    
            if target == nums[pivot]:
                return pivot
            
            if nums[left] <= nums[pivot]:
                if target > nums[pivot] or target < nums[left]:
                    left = pivot + 1
                else:
                    right = pivot - 1
                    
            else:
                if target < nums[pivot] or target > nums[right]:
                    right = pivot - 1
                else:
                    left = pivot +1
                    
        return -1
        
        
S = Solution()
print(S.search([4,5,6,7,0,1,2],0))