# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0

        def dfs(node , min_ = inf, max_ = -inf):
            nonlocal max_diff

            if not node:
                return 0

            min_ = min(min_, node.val)
            max_ = max(max_, node.val)
            max_diff = max(max_diff , max_ - min_)

            dfs(node.left , min_ , max_)
            dfs(node.right , min_ , max_)

        dfs(root)

        return max_diff


        


            




        