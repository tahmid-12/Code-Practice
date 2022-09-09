from typing import List


class Solution(object):
    def longestValidParentheses(self, s):
        result = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i-stack[-1])
        return result
        
        
        

S = Solution()
print(S.longestValidParentheses(")()())"))