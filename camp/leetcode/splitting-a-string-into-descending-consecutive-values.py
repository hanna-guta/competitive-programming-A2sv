class Solution:
    def splitString(self, s: str) -> bool:
        splits = []

        def backtrack(s):
            if not s and len(splits) > 1:
                return True

            for j in range(len(s)):
                var = int(s[:j + 1])
                
                if not splits or var == splits[-1] - 1:
                    splits.append(var)
                    if backtrack(s[j + 1:]):
                        return True
                    splits.pop()

            return False

        return backtrack(s)













""""""
""""""







