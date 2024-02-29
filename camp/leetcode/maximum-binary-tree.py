# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return None

            max_val = max(nums[left:right + 1])
            max_index = nums.index(max_val)

            root = TreeNode(max_val)
            root.left = dfs(left, max_index - 1)
            root.right = dfs(max_index + 1, right)

            return root

        return dfs(0, len(nums) - 1)
