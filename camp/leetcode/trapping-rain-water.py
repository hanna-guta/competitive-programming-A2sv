class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] *  n
        water = [0] * n

        l_max, r_max = height[0], height[n-1]

        for i in range(n):
            if height[i]>l_max:
                l_max = height[i]

            left_max[i]=l_max

        for i in range(n-1, -1, -1):
            if height[i]>r_max:
                r_max = height[i]

            right_max[i]=r_max
        
        for i in range(n):
            if height[i] < min(left_max[i],right_max[i]): 
                water[i] = min(left_max[i],right_max[i]) - height[i]

            else:
                water[i] = 0

                
        return sum(water)