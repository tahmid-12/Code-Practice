from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left,right = 0, len(arr) - k

        while left < right:
            
            pivot = (left + right) // 2
            if x - arr[pivot] <= arr[pivot + k] - x:
                right = pivot
            else:
                left = pivot + 1
    
        return arr[left:left + k]
        
        
S = Solution()
print(S.findClosestElements([1,2,3,4,5],4,3))