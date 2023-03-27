# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sor = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sor.append(node.val)
            inorder(node.right)
        inorder(root)
        ans = inf
        #print(sor)
        for i in range(1,len(sor)):
            ans = min(ans,sor[i]-sor[i-1])
        return ans