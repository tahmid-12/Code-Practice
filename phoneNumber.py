from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letter = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result = []
        for digit in digits:
            if not result:
                result = letter[digit]
            else:
                tmp = []
                for r in result:
                    for l in letter[digit]:
                        tmp.append(r+l)
                result = tmp
        return result
        
        
        
S = Solution()
list = ""
print(S.letterCombinations(list))