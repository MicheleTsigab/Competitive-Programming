class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad=[[] for i in range(numCourses)]
        #length of prerequisites, building the graph
        for i,x in prerequisites:
            ad[i].append(x)
        def is_cycle(node,track):
            track.add(node)
            visited.add(node)
            for child in ad[node]:
                if child not in visited and is_cycle(child,track):
                    return True
                if child in track:
                    return True
            track.remove(node)
            return False
        visited=set()
        for node in range(len(ad)):
            temporary=set()
            if node not in visited:
                if is_cycle(node,temporary):
                    return False
        return True