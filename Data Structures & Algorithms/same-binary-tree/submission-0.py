# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.i = True
        def mas(t: Optional[TreeNode], u: Optional[TreeNode]):
            if not t or not u:
                if not t and not u:
                    return 0
                else:
                    self.i = False
                return 0
            left = mas(t.left, u.left) 
            right = mas(t.right , u.right)
            if t.val != u.val:
                self.i = False
            return 0
        mas(p,q)
        return self.i
            