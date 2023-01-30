class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def search(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return

            if i >=len(candidates) or total > target:
                return
            curr.append(candidates[i])
            search(i+1,curr,total + candidates[i])
            avoid=curr.pop()
            while i < len(candidates) and candidates[i]==avoid:
                i+=1
            search(i,curr,total)
        search(0,[],0)

        return res