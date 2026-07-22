# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        k = head
        fast = head
        prev = None
        nn = slow.next
        while fast and fast.next:
            prev = slow
            slow = slow.next
            nn = slow.next
            fast = fast.next.next
        mid = slow
        
        mid.next = None
        curr = nn
        prev2 = None
        while curr:
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
        while prev2:
            temp = head.next
            head.next = prev2
            head= temp
            temp2 = prev2.next
            prev2.next = head
            prev2 = temp2
        








