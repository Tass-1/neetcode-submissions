# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = []
        for i in range(len(lists)):
            a = lists[i]
            while a:
                k.append(a.val)
                a = a.next
        dum = ListNode(0)
        curr = dum
        m = sorted(k)
        for i in range(len(k)):
            curr.next = ListNode(m[i])
            curr = curr.next
        
        return dum.next
