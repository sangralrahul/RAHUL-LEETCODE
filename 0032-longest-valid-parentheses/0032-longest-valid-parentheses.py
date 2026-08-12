class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])
        return best