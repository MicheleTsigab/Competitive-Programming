# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        a_len = 0
        b_len = 0
        while a or b: #get length
            if a:
                a_len +=1
                a = a.next
            if b:
                b_len +=1
                b = b.next
        a = headA
        b = headB
        k = abs(b_len - a_len)
        if a_len < b_len:  
            while k:
                b = b.next
                k-=1
        else:
            while k:
                a = a.next
                k-=1
        while a and b:
            if a==b:
                return a
            a = a.next
            b = b.next
        return None