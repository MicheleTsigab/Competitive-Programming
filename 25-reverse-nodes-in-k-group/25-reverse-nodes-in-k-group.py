# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
       0 2 1 3 4 5
           l
               r
       r_end = r.next 3 5
       r.next = None
       l_end = l.next 1 3
       reverse(l.next) 1 3
       l_end.next = r_end 5
       right = l_end
       left =  l_end
        """
        dummy = ListNode(0,next=head)
        left = dummy
        right = dummy
        start = ListNode(0)
        while right:
            c = k
            while c and right.next:
                right = right.next
                c-=1
            #print(right.next)
            if not c:

                r_end = right.next
                right.next = None
                l_end = left.next
                st = self.reverse(left.next)
                left.next = right
                l_end.next = r_end
                left = l_end
                right = l_end
                if not start:
                    dummy.next = st
                    start = 1
            else:
                break
        return dummy.next
    def reverse(self,node):
        current=node
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev