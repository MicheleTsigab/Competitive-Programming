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
        
        for i in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return x.next
            
            