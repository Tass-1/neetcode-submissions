# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. The Probe: Find the k-th node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # 2. The Reversal
            # Initialize prev to groupNext so the tail automatically stitches to the remaining list
            prev = groupNext
            curr = groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. The Reconnection
            # tmp holds the old head of the group, which is now the tail
            tmp = groupPrev.next 
            # Link the node before the group to the new head (kth)
            groupPrev.next = kth 
            # Move groupPrev to the tail of this newly reversed group to prepare for the next iteration
            groupPrev = tmp 
            
        return dummy.next

    # Helper function to jump k steps ahead
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr