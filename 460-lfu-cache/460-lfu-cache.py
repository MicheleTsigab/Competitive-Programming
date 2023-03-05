class LFUCache:

    def __init__(self, capacity: int):
        self.freq = {} #freq to dict of keys:None, keys are insertion ordered 
        self.cache = {} #keys to freq
        self.capacity = capacity
        self.min_freq = 1
    def get(self, key: int) -> int:
        #print(f'get {key}',self.freq,self.cache)
        if key not in self.cache:
            return -1
        self.update(key)
        freq = self.cache[key]
        return self.freq[freq][key]
    
    def update(self,key: int) -> None:
        freq = self.cache[key]
        val = self.freq[freq][key]
        
        self.cache[key] = freq + 1
        
        del self.freq[freq][key]
        if freq == self.min_freq and not self.freq[freq]:
            self.min_freq += 1
            
        if not self.freq[freq]:
            del self.freq[freq]
            
        if freq + 1 in self.freq:
            self.freq[freq+1][key]=val 
            self.freq[freq+1].move_to_end(key,last=True)
        else:
            self.freq[freq+1]= OrderedDict()
            self.freq[freq+1][key] = val
        

    def put(self, key: int, value: int) -> None:
        #key exists?, update its frequency
        if key in self.cache:
            self.update(key)
            freq = self.cache[key]
            self.freq[freq][key] = value
            return
        if len(self.cache) == self.capacity:
            #remove LFU, incase of tie, LRU
            k,v = self.freq[self.min_freq].popitem(last=False)
            if not self.freq[self.min_freq]:
                del self.freq[self.min_freq]
                self.min_freq +=1
            del self.cache[k]
        self.min_freq = 1
        self.cache[key]=1
        if 1 in self.freq:
            self.freq[1][key]= value
            self.freq[1].move_to_end(key,last=True)
        else:
            self.freq[1]= OrderedDict()
            self.freq[1][key]=value
        

            
        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)