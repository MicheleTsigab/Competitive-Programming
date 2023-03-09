"""
head -> tail
[3 3]
 h
   t
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.cap = k
        self.cq = [-1] * k
        self.head = 0
        self.tail = -1
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
     #   print(self.tail,  'end ')
        self.tail = (self.tail+ 1) % (len(self.cq)) 
        self.cq[self.tail] = value
        if self.head == -1:
            self.head = 0
        
       
    #    print("eq",self.cq,self.head,self.tail)
        self.size +=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.cq[self.head]=-1
        self.head = (self.head+ 1) % (len(self.cq))
   #     print("deq",self.cq,self.head,self.tail)
        if self.size:
            self.size -=1
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