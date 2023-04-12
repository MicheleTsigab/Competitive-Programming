# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
      
        left,right = self.separate_nodes(head)
        left = self.sortList(left) 
        right = self.sortList(right)
        
        return self.mergeTwoLists(left,right)
        
    def separate_nodes(self, head):
        left = head
        slow = ListNode(0,next=head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        return left,right
    def mergeTwoLists(self, list1,list2):
        left=list1
        right=list2
        head=ListNode()
        merge=head
        while left and right:
            if left.val<right.val:
                merge.next=left
                left=left.next
            else:
                merge.next=right
                right=right.next
            merge=merge.next
        if left:
            merge.next=left
        if right:
            merge.next=right

        return head.next