"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otn = {None:None}
        if not head:
            return None

        curr = head
        while curr:
            otn[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            clone = otn[curr]
            clone.next = otn[curr.next]
            clone.random = otn[curr.random]
            curr = curr.next
        return otn[head]