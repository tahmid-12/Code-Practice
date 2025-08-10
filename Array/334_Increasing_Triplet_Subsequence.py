from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num_i = num_j = float('inf')
        
        for num in nums:
            if num <= num_i:
                num_i  = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False        
        
        
S = Solution()
print(S.increasingTriplet([2,1,5,0,4,6]))
