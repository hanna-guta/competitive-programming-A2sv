class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing_number = 1
        i = 0 
        patches = 0

        while missing_number <= n:
            if i < len(nums) and nums[i] <= missing_number:
                missing_number += nums[i]
                i += 1
            else:
                missing_number += missing_number
                patches += 1

        return patches

        




























  
    
 


    
        