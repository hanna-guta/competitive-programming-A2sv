class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for bracket in s:
            if bracket == '(' or len(stack) == 0 or (stack and stack[-1] != '('):
                stack.append(bracket)
            else:
                stack.pop()

        return len(stack)