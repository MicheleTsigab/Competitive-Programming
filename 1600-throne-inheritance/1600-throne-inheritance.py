class ThroneInheritance:

    def __init__(self, kingName: str):
        self.g = defaultdict(list)
        self.alive = defaultdict(bool)
        self.king = None
    def birth(self, parentName: str, childName: str) -> None:
        if not self.king:
            self.king = parentName
        self.g[parentName].append(childName)
        self.alive[parentName] = True
        self.alive[childName] = True
    def death(self, name: str) -> None:
        self.alive[name]=False

    def getInheritanceOrder(self) -> List[str]:
        seen = set()
        ans = []
        def dfs(node):
            seen.add(node)
            if self.alive[node]:
                ans.append(node)
            for ch in self.g[node]:
                if ch not in seen:
                    dfs(ch)
        dfs(self.king)
        if not ans:
            return ['king']
        return ans
                    


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()