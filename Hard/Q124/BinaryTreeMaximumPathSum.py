import collections
# excellent job

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.dp(root))

    def dp(self, cur: TreeNode) -> tuple:
        left, right = (-float("inf"), -float("inf")), (-float("inf"), -float("inf"))
        if cur.left is not None:
            left = self.dp(cur.left)
        if cur.right is not None:
            right = self.dp(cur.right)
        return max(left[0], right[0], 0) + cur.val, max(max(left[0], 0) + max(right[0], 0) + cur.val, left[1], right[1])


n6 = TreeNode(7, None, None)
n5 = TreeNode(15, None, None)
n2 = TreeNode(20, n5, n6)
n1 = TreeNode(9, None, None)
n0 = TreeNode(-10, n1, n2)

sol = Solution()
print(sol.maxPathSum(n0))
