# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 2 3 4 5
              x   y
        """
        if head.next == None:
            return None
        x = ListNode(next = head)
        left = x
        right = x.next
        
        while right or n:
            if n:
                right = right.next
                n-=1
                continue
            right = right.next
            left = left.next
            
            
        left.next = left.next.next
        return x.next
            
            