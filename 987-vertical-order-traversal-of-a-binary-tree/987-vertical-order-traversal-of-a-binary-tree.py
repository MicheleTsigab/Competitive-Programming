# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_heap = []
        q = deque()
        row = 0
        col = 0
        q.append([root,row,col]) #node,vertical pos
        
        while q:
            node, row,col = q.popleft()
            
            heapq.heappush(min_heap,[col,row,node.val])
            if node.left:
                q.append([node.left,row+1,col-1])
            if node.right:
                q.append([node.right,row+1,col+1])
        #print(min_heap)
        res = []
        while min_heap:
            vpos,row,node = heapq.heappop(min_heap)
            temp = []
            temp.append(node)
            
            while min_heap and min_heap[0][0] == vpos:
                temp.append(heapq.heappop(min_heap)[2])
                
            res.append(temp)
        return res
                