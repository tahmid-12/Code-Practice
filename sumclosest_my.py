from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        print(nums)
        print("Target =>", target)
        sum = 0
        triplet = []
        if len(set(nums)) == 0:
            return 0
        else:
            for i in range(len(nums)):
                sum = sum + nums[i]
                triplet.append(nums[i])
                if sum - target == 1:
                    break
        
        print("Sum =>", sum)
        print("Triplet =>", triplet)
        return sum
        
        
        
S = Solution()
S.threeSumClosest([-1,2,1,-4],1)
S.threeSumClosest([0,0,0],1)