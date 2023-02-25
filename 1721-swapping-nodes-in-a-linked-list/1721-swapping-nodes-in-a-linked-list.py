# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,next=head)
        slow = dummy
        left = dummy
        fast = dummy.next
        for i in range(k):
            fast = fast.next
            left = left.next


        while fast:
            slow=slow.next
            fast = fast.next

        slow.next.val,left.val = left.val,slow.next.val
        return dummy.next