# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None for _ in range(k)]
        current = head
        slow = head
        length = 0
        while current:
            current = current.next
            length += 1
        rem = length % k
        part = length // k
        for i in range(len(result)):
            lst = slow
            result[i]=lst
            p = part + 1 if i < rem else part
            for j in range(p-1):
                if lst:
                    lst= lst.next
            if lst:
                lst.next,slow = None,lst.next
            
        return result