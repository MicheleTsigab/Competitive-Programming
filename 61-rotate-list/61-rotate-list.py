# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1 2 3 4 5
        5 4 / 3 2 1
        4 5 -> 1 2 3
        """
        if not head or not head.next:
            return head
        n = 0
        dummy = ListNode(0,next=head)
        fast = dummy
        slow = dummy
        while fast.next:
            fast = fast.next
            n+=1
        k = k % n
        k= n - k
        while k:
            slow = slow.next
            k-=1
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next
        