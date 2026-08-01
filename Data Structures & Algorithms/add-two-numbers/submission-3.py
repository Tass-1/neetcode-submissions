# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dig1 = []
        dig2 = []
        curr1 = l1
        curr2 = l2
        while curr1:
            dig1.append(curr1.val)
            
            curr1 = curr1.next
            
        while curr2:
            dig2.append(curr2.val)
            curr2 = curr2.next
        sum1 = 0
        sum2 = 0
        i = 0
        j =0
        while i < len(dig1):
             sum1 = sum1 + (dig1[i]*(10**i))
             i+=1
        while j < len(dig2):
             sum2 = sum2 + (dig2[j]*(10**j))
             j+=1
        print(sum1)
        print(sum2)
        print(dig2)
        sum3 = sum1 + sum2
        dig3 = []
        for k in range(len(str(sum3))):
            dig3.append(sum3%10)
            sum3 = sum3//10


        dum = ListNode(7)
        curr = dum
        for m in range(len(dig3)):
            curr.next = ListNode(dig3[m])
            curr = curr.next
        return dum.next







        