# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        current = head
        while current:
            next_node = current.next
            prev = dummy
            while prev.next and current.val >= prev.next.val:
                prev = prev.next
            prev.next,current.next = current, prev.next
            current = next_node

        return dummy.next
            
            