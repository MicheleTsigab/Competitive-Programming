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
        q.append([root,row,col]) #node,vertical pos
        
        while q:
            node, row,col = q.popleft()
            
            arr.append([col,row,node.val])
            if node.left:
                q.append([node.left,row+1,col-1])
            if node.right:
                q.append([node.right,row+1,col+1])

        res = []
        arr.sort()
        comp = arr[0][0]
        temp = []
        for col,row,node in arr:
            if col == comp:
                temp.append(node)
            else:
                res.append(temp)
                comp = col
                temp = [node]
        if res[-1][-1] != temp[0]:
            res.append(temp)
        return res
                