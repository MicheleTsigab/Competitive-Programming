# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def find(node,path):
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append('->'.join(path))
                path.pop()
                return
            
            if node.left:
                find(node.left,path)
            
            if node.right:
                find(node.right,path)
            path.pop()
        find(root,[])
        return res
            