class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        arr = []

        def backtrack(idx, subset):
            arr.append(subset[:])

            for i in range(idx, N):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return arr
