from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        
        while left<=right:
            pivot=(left+right)//2
            if arr[pivot-1]<arr[pivot] and arr[pivot]>arr[pivot+1]:
                return pivot
            elif arr[pivot]<arr[pivot+1]:
                left=pivot+1
            else:
                right=pivot-1
        
        
S = Solution()
list = [0,10,5,2]
print(S.peakIndexInMountainArray(list))