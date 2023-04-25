class SmallestInfiniteSet:

    def __init__(self):
        self.s = {i for i in range(1,1001)}
        
        

    def popSmallest(self) -> int:
        x = min(self.s)
        self.s.remove(x)
        return x
    def addBack(self, num: int) -> None:
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)