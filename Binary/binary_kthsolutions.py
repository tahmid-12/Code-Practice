from typing import List

class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
    left, right = 0, len(arr) 
    while left < right:
      pivot = left + (right - left) // 2
      if arr[pivot] - (pivot + 1) >= k:
        right = pivot
      else:
        left = pivot + 1
    return left + k
    
S = Solution();
print(S.findKthPositive([2,3,4,7,11],5))