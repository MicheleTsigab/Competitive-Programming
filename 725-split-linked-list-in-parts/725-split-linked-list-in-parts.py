# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None for _ in range(k)]
        dummy = ListNode(0,next=head)
        current = dummy
        slow = head
        fast = dummy
        length = 0
        while current.next:
            current = current.next
            length += 1
        rem = length % k
        part = length // k
        part_1 = part + 1
        for i in range(len(result)):
            lst = slow
            result[i]=lst
            p = part_1 if i < rem else part
            for j in range(p-1):
                if lst:
                    lst= lst.next
            if lst:
                prev = lst
                slow = lst.next
                prev.next = None
            
        return result