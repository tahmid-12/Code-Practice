from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        
        while left <= right:
            pivot = (left + right // 2)
            total = 0
            for num in nums:
                if num > pivot:
                    total += (num - 1) // pivot
            if total > maxOperations:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left
        
        
S = Solution()
# print(S.minimumSize([2,4,8,2],4))
print(S.minimumSize([9],2))