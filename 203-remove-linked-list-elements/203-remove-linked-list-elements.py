# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        ans = dummy
        ans_head = ans
        
        while head:
            if head.val!=val:
                ans.next = head
                ans = ans.next
            head = head.next
        if ans and ans.next and ans.next.val == val:
            ans.next = None
        return ans_head.next