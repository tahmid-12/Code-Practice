from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for numbers in nums:
            if numbers in hashset:
                return True
            hashset.add(numbers)
    
    
S = Solution()
print(S.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))