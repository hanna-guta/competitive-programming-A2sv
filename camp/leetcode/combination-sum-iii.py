from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, n, comb):
            if n == 0 and len(comb) == k:
                ans.append(comb[:])
                return 

            for i in range(idx, 9):
                if len(comb) < k:
                    comb.append(i + 1)
                    backtrack(i + 1, n - i - 1, comb) 
                    comb.pop()

        backtrack(0, n, [])
        return ans
