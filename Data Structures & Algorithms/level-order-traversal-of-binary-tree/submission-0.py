from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        k = []
        if not root:
            return k
        q = deque([root])
        while q:
            curr = []
            lev = len(q)
            for i in range(lev):
                no = q.popleft()
                curr.append(no.val)
                if no.left:
                    q.append(no.left)
                if no.right:
                    q.append(no.right)
            k.append(curr)
        return k