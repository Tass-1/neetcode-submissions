# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxDia = 0
        def maxD(toot: Optional[TreeNode]):
            if not toot:
                return 0
            left = maxD(toot.left)
            right = maxD(toot.right)
            self.maxDia = max(self.maxDia , left + right)
            return max(left, right) + 1
        maxD(root)
        return self.maxDia










