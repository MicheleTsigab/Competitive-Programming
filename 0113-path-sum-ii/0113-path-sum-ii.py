# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def find(node,path,total):
            path.append(node.val)
            total += node.val
            
            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path.copy())
                total-=path.pop()
                return
            
            if node.left:
                find(node.left,path,total)
            
            if node.right:
                find(node.right,path, total)
                
            total-=path.pop()
        find(root,[],0)
        return res