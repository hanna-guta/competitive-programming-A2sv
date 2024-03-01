class Solution:
    def totalNQueens(self, n: int) -> int:
        matrix = [['.'] * n for i in range(n)]

        col_set = set()
        pos_diagonal = set()
        neg_diagonal = set()

        ans = []

        def backtrack(row):
            if row == n:
                ans.append([''.join(row) for row in matrix])
                return
            
            for col in range(n):
                if col in col_set or (row + col) in pos_diagonal or (row - col) in neg_diagonal:
                    continue

                matrix[row][col] = 'Q'

                col_set.add(col)
                pos_diagonal.add((row + col))
                neg_diagonal.add((row - col))

                backtrack(row + 1)

                col_set.remove(col)
                pos_diagonal.remove((row + col))
                neg_diagonal.remove((row - col))
                matrix[row][col] = '.'
        
        backtrack(0)
        return len(ans)

        
        