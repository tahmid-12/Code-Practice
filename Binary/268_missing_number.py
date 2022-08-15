from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        visited = set()
        
        for num in nums:
            visited.add(num)
        
        for i in range(0, n + 1):
            if i not in visited:
                return i


S = Solution()
print(S.missingNumber([3,0,1]))