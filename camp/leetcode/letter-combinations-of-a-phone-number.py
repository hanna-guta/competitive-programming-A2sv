class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash_map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        comb = []
        ans = []
        
        if not digits:
            return []

        def backtrack(digits):
            nonlocal comb

            if not digits:
                ans.append("".join(comb))
                return 

            for c in hash_map[int(digits[0])]:
                comb.append(c)
                backtrack(digits[1:])
                comb.pop()

        backtrack(digits)
        return ans
