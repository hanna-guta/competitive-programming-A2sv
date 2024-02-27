class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx):

            if idx == len(nums):
                ans.append(nums[:])
                return 

            for i in range(idx , len(nums)):
                nums[idx] , nums[i] = nums[i] , nums[idx]
                backtrack(idx + 1)
                nums[idx] , nums[i] = nums[i] , nums[idx]
        backtrack(0)
        return ans
            
    