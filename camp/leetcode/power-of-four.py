class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if not n:
            return False
        if n % 4 == 0:
            return self.isPowerOfFour(n/4)
        else:
            return False

        
