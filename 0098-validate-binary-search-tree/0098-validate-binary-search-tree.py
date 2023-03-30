# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(lb,ub,node):
            if not node:
                return True
            if node.val <= lb:
                return False
            if node.val >= ub:
                return False

            left_bool = isvalid(lb, node.val,node.left)
            right_bool = isvalid(node.val,ub,node.right)
            return left_bool and right_bool
        return isvalid(-inf,inf,root)