class ListNode:
    def __init__(self,val=-1,next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.dt = [ListNode(-1) for _ in range(10**4)]
        self.MOD = 10**4

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = key % self.MOD
        n = self.dt[idx]
        while n.next:
            n = n.next
        n.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
       # print(key)
        idx = key % self.MOD
        n = self.dt[idx]
        while n.next.val!=key:
            
            n = n.next
       # print(n.val,n.next.next.val, n.next.val)
        n.next = n.next.next
    def contains(self, key: int) -> bool:
        idx = key % self.MOD
        n = self.dt[idx]
        if n.val == key:
            return True
        while n.next:
            n = n.next
            if n.val == key:
                return True
            
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)