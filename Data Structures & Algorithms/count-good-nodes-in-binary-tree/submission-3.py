# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        k = 0
        m=[]
        t = root.val
        ma = 0
        def isa(root: Optional[TreeNode], maxfar):
            nonlocal k
            if not root:
                return 

            if root.val >= maxfar:
                k += 1
            maxfar = max(maxfar,root.val)
            isa(root.left, maxfar)
            isa(root.right , maxfar)

        isa(root,root.val)
        return k
