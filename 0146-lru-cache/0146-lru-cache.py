class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.mru=self.lru=Node(0,0)
        self.lru.next,self.mru.prev=self.mru,self.lru
    def remove(self,node:Node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self,node):
        oldNode=self.mru.prev
        self.mru.prev=node
        oldNode.next=node
        node.next=self.mru
        node.prev=oldNode
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from any position it is
            self.remove(self.cache[key])
            # put it previous to MRU
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            lru=self.lru.next
            self.remove(lru)
            del self.cache[lru.key]                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)