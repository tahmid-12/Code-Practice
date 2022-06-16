# dic = {}

# for i in range(3):
#     dic[i] = {}
    
# print(dic)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        dic = {}
        # print(n)
        
        for i in range(numRows):
            dic[i] = []
        
        row = 0
        for i in range(n):
            dic[row].append(s[i])
            
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            
            row += step
        
        result = ''
        for i in dic:
            for j in dic[i]:
                result += j
        return result
        

arr = Solution()
print(arr.convert("PAYPALISHIRING",3))
arr2 = Solution()
print(arr.convert("PAYPALISHIRING",4))
