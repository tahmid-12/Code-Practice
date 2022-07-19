from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # If no number then return 0
        if not any(map(bool, nums)):
            return '0'
            
        # Mapping interger to string
        nums = list(map(str, nums))
        
        # if length less than two then return the value after join
        if len(nums) < 2:
            return "".join(nums)
        
        # Compare 2 digits after adding them in both ways like x+ y and y + x
        def compare(x, y):
            return (int(nums[x]+nums[y])) > (int(nums[y]+nums[x]))
        
        # Compare 2 digits in the list and then after compare then join them and after finishing it join the numbers.
        for x in range(len(nums) - 1):
            y = x + 1
            while x < len(nums) and y < (len(nums)):
                if not compare(x,y):
                    nums[y], nums[x] = nums[x], nums[y]
                y+=1

        return "".join(nums)   
        
S = Solution()
nums = [2, 20, 24, 6, 8]
print(S.largestNumber(nums))
