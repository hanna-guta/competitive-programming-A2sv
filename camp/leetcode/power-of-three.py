class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        counter = 1
        while counter < n:
            counter *= 3
        return counter == n
        