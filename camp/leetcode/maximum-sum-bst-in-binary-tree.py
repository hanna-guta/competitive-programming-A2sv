class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def valid(node, left_max, right_min):
            if not node:
                return True, 0, inf, -inf

            left_valid, left_sum, left_min, left_max = valid(node.left, left_max, node.val)
            right_valid, right_sum, right_min, right_max = valid(node.right, node.val, right_min)

            if left_valid and right_valid and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                ans[0] = max(ans[0], curr_sum)

                return True, curr_sum, min(left_min, node.val), max(right_max, node.val)
            else:
                return False, 0, 0, 0

        valid(root, -inf, inf)
        return ans[0]



