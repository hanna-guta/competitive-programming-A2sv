class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [max(row) for row in grid]
        col = [max(col) for col in zip(*grid)]

        summ = 0
        for i in range(n):
            for j in range(n):
                summ += min(row[i], col[j]) - grid[i][j]

        return summ
                