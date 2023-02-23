# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        a=[]
        while current:
            a.append(current.val) 
            current=current.next
        l=0
        r=len(a)-1
        while l<r:
            if a[l]!=a[r]:
                return False
            l+=1
            r-=1
        return True