from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        distance = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                distance = max(distance, j - i)
                j += 1
        return distance



S = Solution()
print(S.maxDistance([55,30,5,4,2],[100,20,10,10,5]))