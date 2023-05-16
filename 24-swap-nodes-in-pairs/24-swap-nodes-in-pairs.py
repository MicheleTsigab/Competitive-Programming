# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        0 1 2 3
        l r r.next
        l.next = r.next
        r.next = r.next.next
        r.next.next = r
        l r
        l.next = r.next
        r.next = l.next
        
        l.nxt = 2(r) 0->2
        temp = left.next
        temp2 = right.next
        r.nxt = l.nxt(1) 
        temp.next = temp2.next
        
        2 1 3 4
          l r
        l = 0,2
        r = 1,4
        """
        if not head or not head.next:
            return head
        left = ListNode(0,head)
        dum = left
        right = head
        while left and right and right.next:
            x = right
            tempr = right.next
            left.next,right.next, = right.next,right.next.next
            if tempr:
                tempr.next = x
            left = x
            right = x.next if x else None
        return dum.next