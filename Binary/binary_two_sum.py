from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        sum = 0
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1,right + 1]
      
        
S = Solution();
print(S.twoSum([2,7,11,15],9))