class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def rec(n):
            if n == 1:
                return 5  
            if n % 2 == 0:
                return (self.pow_mod(5, n // 2) * self.pow_mod(4, n // 2)) % (10**9 + 7)
            else:
                return (self.pow_mod(5, n // 2 + 1) * self.pow_mod(4, n // 2)) % (10**9 + 7)
        
        return rec(n)
    
    def pow_mod(self, base, exp):
        res = 1
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % (10**9 + 7)
            base = (base * base) % (10**9 + 7)
            exp //= 2
        return res
