# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left-=1
        dummy = ListNode(0,head)
        left_node = dummy
        right_node = dummy
        while left > 0:
            left_node = left_node.next
            left -=1
        while right > 0:
            right_node = right_node.next
            right -=1
        right_most = right_node.next
        right_node.next = None
        left_most = left_node.next
        self.reverse_list(left_node.next)
        left_node.next = right_node
        left_most.next = right_most
        
        return dummy.next
    def reverse_list(self,node):
        next=None
        prev=None
        current=node
        last = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev