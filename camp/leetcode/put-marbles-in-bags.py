class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        if n <= 2 or n == k:
            return 0

        part = [0] * (n - 1)

        for i in range(n - 1):
            part[i] = weights[i]+weights[i+1]

        part.sort()

        return sum(part[n-k:])  - sum(part[:k-1])