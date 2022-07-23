from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,nums[-1] + 1):
            while i > nums[0]:
                nums.pop(0)
            if len(nums) == i:return i
        return -1


S = Solution()
print(S.specialArray([3,5]))