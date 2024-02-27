class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def backtrack(idx, target, comb):
            if target < 0:
                return 
            if target == 0:
                ans.append(comb[:])
                return 

            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, target - candidates[i], comb) 
                comb.pop()

        backtrack(0, target, [])
        return ans
