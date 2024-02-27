# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_count = count = 0
        prev_val = float('-inf')
        arr = []
        def dfs(node):
            nonlocal max_count, count, prev_val, arr
            
            if not node:
                return

            dfs(node.left)

            if node.val == prev_val:
                count += 1
            else:
                count = 1

            if count == max_count:
                arr.append(node.val)

            elif count > max_count:
                max_count = count
                arr = [node.val]

            prev_val = node.val

            dfs(node.right)

      

        dfs(root)

        return arr
