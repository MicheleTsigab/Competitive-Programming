class Solution:
    def maxLength(self, arr: List[str]) -> int:        
        count = [0]
        def search(i,curr):
            if curr or i==len(arr):
                x=''.join(curr)
                if len(set(x))==len(x):
                    count[0]=max(count[0], len(x))
            if i>=len(arr):    
                return
            curr.append(arr[i])
            search(i+1,curr)
            curr.pop()
            search(i+1,curr)
        search(0,[])
        return count[0]
 