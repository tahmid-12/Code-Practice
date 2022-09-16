from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        point1 = point2 = 0
        new_array = []
        
        while point1!=len(nums1) and point2!=len(nums2):
            if nums1[point1] == nums2[point2]:
                new_array.append(nums1[point1])
                point1 += 1
                point2 += 1
            else:
                if nums1[point1] > nums2[point2]:
                    point2 += 1
                else:
                    point1 += 1
                
        return new_array


S = Solution()
print(S.intersect([1,2,2,1],[2,2]))