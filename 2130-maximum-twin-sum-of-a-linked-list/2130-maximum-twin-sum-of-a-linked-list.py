# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        5 4 1 2
        l
              r
        #reverse second half
        #compute max sum
        """
        dummy = ListNode(0,head)
        fast = dummy
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        right = self.reverse(slow)
        left = head
        max_sum = 0
        while right and left:
            max_sum = max(max_sum,right.val + left.val)
            left= left.next
            right= right.next
        return max_sum
    def reverse(self,node):
        current=node
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev