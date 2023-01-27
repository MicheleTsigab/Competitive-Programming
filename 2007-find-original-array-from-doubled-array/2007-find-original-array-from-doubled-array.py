class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count=Counter(changed)
        res =[]
        for i in changed:
            if i in count and i*2 in count: 
                res.append(i)
                count[i]-=1
                count[i*2]-=1
                if count[i]<=0:
                    del count[i]
                if count[i*2]<=0:
                    del count[i*2]
        if len(res)*2==len(changed) and len(count)==0:
            return res
        else:
            []
        