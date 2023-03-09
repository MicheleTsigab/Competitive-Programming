"""
head -> tail
[3 3]
 h
   t
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.size,self.head,self.tail = 0,0,0
        self.cap = k
        self.cq = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():

            self.tail = (self.tail+ 1) % self.cap
        self.cq[self.tail] = value
        
        self.size +=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.cq[self.head]=-1
        
        self.head = (self.head+ 1) % (self.cap)

        if self.size:
            self.size -=1
        
        if self.isEmpty():
            self.tail = self.head
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0        

    def isFull(self) -> bool:
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()