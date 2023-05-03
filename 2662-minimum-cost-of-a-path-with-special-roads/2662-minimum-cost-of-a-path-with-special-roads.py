class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        pq = [(0,start[0],start[1])]
        edge = defaultdict(list)
        for x1,y1,x2,y2,c in specialRoads:
            if abs(y2-y1) + abs(x2-x1) < c:
                continue
            edge[(x1,y1)].append((x2,y2,c))
        seen = set()
        while pq:
            cost,x1,y1 = heapq.heappop(pq)
            if x1 == target[0] and y1 == target[1]:
                return cost
            if (x1,y1) in seen:
                continue
            seen.add((x1,y1))
            #x1,y1 is a start of special roads
            for x2,y2,c in edge[(x1,y1)]:
                if (x2,y2) not in seen:
                    heapq.heappush(pq,(cost + c,x2,y2))
            
            #current pos to start of any special roads
            for px1,py1 in edge:
                if (px1,py1) not in seen:
                    heapq.heappush(pq,(cost + abs(py1 - y1) + abs(px1 - x1),px1,py1))
                    
            
            #current pos to target
            heapq.heappush(pq,(cost + abs(target[0] - x1) + abs(target[1] - y1),target[0],target[1]))
        
            
            
            