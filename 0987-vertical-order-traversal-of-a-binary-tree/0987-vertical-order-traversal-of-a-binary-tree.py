# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = deque()
        row = 0
        col = 0
        q.append([root,row,col]) 
        
        while q:
            node, row,col = q.popleft()
            
            arr.append([col,row,node.val])
            if node.left:
                q.append([node.left,row+1,col-1])
            if node.right:
                q.append([node.right,row+1,col+1])

        res = []
        arr.sort()
        prev_col = arr[0][0]
        for col,row,node in arr:
            if not res or col != prev_col: #if new node with new column
                res.append([node])
                prev_col = col
            else:
                res[-1].append(node)
        return res
                