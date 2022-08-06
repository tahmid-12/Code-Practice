from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums)
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] and nums[high-1] == nums[mid]:
                low +=1
                high -=1
                continue
            if nums[low]<=nums[mid]:
                if target >=nums[low] and target <nums[mid]:
                   high = mid
                else:
                   low = mid+1
            else:
                if target<=nums[high-1] and target>nums[mid]:
                   low = mid+1
                else:
                   high = mid
        return False


S = Solution()
print(S.findMin([4,5,6,7,0,1,2]))