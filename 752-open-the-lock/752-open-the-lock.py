class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(i for i in deadends)
        if target in deadends or '0000' in deadends:
            return -1
        q = deque()
        q.append('0000')
        seen = set()
        seen.add('0000')
        parent = dict()
        l = 0
        while q:
        #    print(q)            
            for _ in range(len(q)):

                n = q.popleft()
                if n == target:
                    return l

                for i in range(4):
                    x = list(n)
                    if x[i]!='9':
                        x[i] = chr((ord(n[i]) + 1))
                    else:
                        x[i] = '0'
                    p = ''.join(x)
                    if p not in seen and p not in deadends:
                        q.append(p)
                        parent[p] = n
                        seen.add(p)
                for i in range(4):
                    x = list(n)
                    if x[i]!='0':
                        x[i] = chr((ord(n[i]) - 1))
                    else:
                        x[i] = '9'
                    p = ''.join(x)
                    if p not in seen and p not in deadends:
                        q.append(p)
                        parent[p] = n
                        seen.add(p)
                
        
            l+=1
        return -1