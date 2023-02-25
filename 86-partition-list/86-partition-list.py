# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        [1,4,3,2,5,2], x = 3
             r.next
         l = head
         r = head
        """
        if not head:
            return None
        dummy = ListNode(0,next=head)
        if head.val < x:
            l = head
        else:
            l = dummy
        r = head
        while r:
            right = r.next
            if r.next and r.next.val < x:
                #delete
                less = r.next
                r.next = r.next.next
                temp = l.next
                #insert at left
                l.next,less.next = less,l.next
                l = l.next
            r = right
        return dummy.next