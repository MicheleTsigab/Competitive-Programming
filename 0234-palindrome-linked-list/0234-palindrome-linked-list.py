
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        1->2->2->1
              l   r
        find middle
        reverse the right part to 1->2
        compare and return bool (1->2 and 1->2)
        
        """
        dummy = ListNode(0,next=head)
        left = head
        right = dummy #to slow down right pointer because we want left to be before middle
        
        # find the middle of the list
        while right.next and right.next.next:
            left = left.next
            right = right.next.next
        
        # reverse the right part of the list
        reversed_node = self.reverse_list(left)
        left = head
        
        # compare the values to determine if palindrom
        while left and reversed_node:
            if left.val != reversed_node.val:
                return False
            left = left.next
            reversed_node = reversed_node.next
        return True
    
    def reverse_list(self,node):
        next=None
        prev=None
        current=node
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
            
    