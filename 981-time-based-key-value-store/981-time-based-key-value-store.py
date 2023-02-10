class TimeMap:

    def __init__(self):
        self.tmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append((timestamp,value))
        else:
            self.tmap[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ''
        arr = self.tmap[key]
        low, high = 0, len(arr) - 1
        ans = [0,'']
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid][0]<=timestamp:
                low = mid + 1
                if arr[mid][0] > ans[0]:
                    ans[0] = arr[mid][0]
                    ans[1] = arr[mid][1]
            else:
                high = mid - 1
        return ans[1]
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)