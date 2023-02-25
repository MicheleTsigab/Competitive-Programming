# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0,next=head)
        left = dummy.next
        right = dummy.next.next
        while left and right:
            left.val,right.val=right.val,left.val
            #print(left,right)
            left=right.next
            right =left.next if left else None
        return dummy.next