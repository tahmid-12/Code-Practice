from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) - 1,1,-1):
            j,k = 0, i - 1
            while j<k:
                if nums[j] + nums[k] > nums[i]:
                    result += k - j
                    k -= 1
                else:
                    j += 1
        return result
        
                
S = Solution()
print(S.triangleNumber([2,2,3,4]))