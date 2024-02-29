# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vertical = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return

            vertical[col].append((row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        ans = []
        for col in sorted(vertical.keys()):
            sorted_nodes = sorted(vertical[col])
            ans.append([val for key, val in sorted_nodes])

        return ans
