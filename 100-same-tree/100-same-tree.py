# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def search(p,q):
            if p==None and q==None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return search(p.left,q.left) and search(p.right,q.right)
        return search(p,q)