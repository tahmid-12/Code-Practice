from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if len(letters) == 0:
            return 0
            
        else:
            left = 0
            right = len(letters)
        
            while left < right:
              pivot = left + (right - left)  // 2
              if letters[pivot] <= target:
                left = pivot + 1
              else:
                right = pivot
        
            return letters[left % len(letters)]
        
S = Solution()
nums, t = ["c","f","g"], "a"
print(S.nextGreatestLetter(nums,t))