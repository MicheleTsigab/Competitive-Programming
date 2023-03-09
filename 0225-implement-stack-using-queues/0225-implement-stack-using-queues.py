class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_ = 0
        

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_ = x

    def pop(self) -> int:
        
        q2 = deque()
        while len(self.q) > 1:
            x =self.q.popleft()
            q2.append(x)
            self.top_ = x
        last = self.q.popleft()
        self.q = q2
        return last

    def top(self) -> int:
        return self.top_

    def empty(self) -> bool:
        return not len(self.q)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()