# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.v = True
        p = root.val
        def isF(root: Optional[TreeNode] , low , high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return isF(root.left , low, root.val) and isF(root.right, root.val, high)
            
        return isF(root ,float('-inf') , float('inf'))
    