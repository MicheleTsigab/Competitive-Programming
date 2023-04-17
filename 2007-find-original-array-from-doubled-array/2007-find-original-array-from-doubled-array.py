class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count=Counter(changed)
        res =[]
        for i in changed:
            if count[i] and count[i*2]: 
                res.append(i)
                count[i]-=1
                count[i*2]-=1
        if len(res)*2==len(changed) and all(not count[i] for i in count):
            return res
        
        return []
        