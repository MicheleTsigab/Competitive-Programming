class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.val if node else -1
    
    def get_node(self, index,before=False):
        if index>=self.size:
            return None
        current = ListNode(0,self.head)
        while index:
            current = current.next
            index -=1
        if before:
            return current
        return current.next
        
    
    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val,self.head)
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if not self.size:
            self.addAtHead(val)
            return
        current = ListNode(0,self.head)
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
        node = self.get_node(index,before=True)
        if not node:
            return
        
        node.next = ListNode(val,node.next)
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        node = self.get_node(index,before=True)
        if not node:
            return
        if node.next == self.head:
            self.head = self.head.next
        else:
            node.next = node.next.next 
        self.size -=1
        if self.size <0:
            self.size = 0
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)