class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(idx, row, col):
            if idx == len(word):
                return True
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] != word[idx] or board[row][col] == "!":
                return False

            first_char = board[row][col]
            board[row][col] = "!"

            top = backtrack(idx + 1, row - 1, col)
            right = backtrack(idx + 1, row, col + 1)
            bottom = backtrack(idx + 1, row + 1, col)
            left = backtrack(idx + 1, row, col - 1)

            board[row][col] = first_char

            return top or right or bottom or left

        def valid(board , word):

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        if backtrack(0, i, j):
                            return True

            return False
        return valid(board , word)

