# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        i = 1
        dummy=ListNode(0,next=head)
        odd_nodes = dummy
        even_nodes = dummy
        even_head = head.next
        ptr = dummy.next
        while ptr:

            if i%2!=0:#odd
                odd_nodes.next = ptr
                odd_nodes = ptr
                
            else:
                even_nodes.next = ptr
                even_nodes = ptr
                
            ptr=ptr.next
            i+=1
            
        odd_nodes.next = even_head
        even_nodes.next = None

        return head