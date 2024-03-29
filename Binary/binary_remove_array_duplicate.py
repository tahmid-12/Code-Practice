from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        pre = 0
        for cur in range(1,len(nums)):
            if nums[cur]!=nums[pre]:
                pre+=1
                nums[pre]=nums[cur]

        return pre+1
        
S = Solution();
print(S.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))