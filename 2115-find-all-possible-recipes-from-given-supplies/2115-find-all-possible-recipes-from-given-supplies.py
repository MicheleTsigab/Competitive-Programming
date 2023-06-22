class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        #build graph
        ed = defaultdict(list)
        inc = defaultdict(int)
        
        for i in range(len(recipes)):
            re = recipes[i]
            for j in ingredients[i]:
                ed[j].append(re)
                inc[re]+=1
     #   print(ed)
        q = deque()
        order = set()
        for i in supplies:
            q.append(i)
       #top sort 
        while q:
            node = q.popleft()
     #       print(node)
            order.add(node)
            for nei in ed[node]:
                inc[nei]-=1
                if inc[nei] == 0:
                    q.append(nei)
        ans = []
        #check which recipe can be made
        for i in recipes:
            if i in order:
                ans.append(i)
        return ans