# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = None
        def inorder(node):
            nonlocal ans,prev
            if not node:
                return
            inorder(node.left)
            if prev:
                ans = min(ans,node.val - prev.val)
            prev = node
            inorder(node.right)
        inorder(root)
        return ans