class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(open, close, curr):
            if open == close == 0:
                ans.append("".join(curr))
                return
            
            if open :
                curr.append("(")
                backtrack(open - 1, close , curr)
                curr.pop()
            if close > open:
                curr.append(")")
                backtrack(open, close - 1 , curr)
                curr.pop()
        
        backtrack(n, n, [])
        return ans
