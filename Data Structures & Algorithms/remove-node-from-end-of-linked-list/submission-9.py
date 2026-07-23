# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn 
        prev2 = None
        k = prev
        if n == 1:
            k = k.next
        else:
            for i in range(n):
                
                if i == n-1:
                    prev2.next = prev.next
                    prev.next = None
                prev2 = prev
                prev = prev.next
        
        curr2 = k
        prev3 = None
        while curr2:
            nn2 = curr2.next
            curr2.next = prev3
            prev3 = curr2
            curr2 = nn2
        return prev3