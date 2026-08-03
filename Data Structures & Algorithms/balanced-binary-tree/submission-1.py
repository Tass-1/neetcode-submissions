# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.bal = True
        def mas(toot: Optional[TreeNode]):
            if not toot:
                return 0
            left = mas(toot.left)
            right = mas(toot.right)
            if left or right:
                if abs(left-right)>1:
                    self.bal = False
            
            return max(left,right)+1
        mas(root)
        return self.bal