from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        comb = []
        
        def backtrack(idx, target):
            nonlocal comb
            if target == 0:
                ans.append(comb.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] <= target:
                    comb.append(candidates[i])
                    backtrack(i + 1, target - candidates[i])
                    comb.pop()
        
        backtrack(0, target)
        return ans
