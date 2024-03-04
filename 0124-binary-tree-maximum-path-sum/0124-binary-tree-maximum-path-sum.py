# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        
        
        def find(node):
            """
            returns max sum without split for each node
            while also updating the global variable with the max sum with splitting
            """
            nonlocal ans
            if not node:
                return 0
            maxleft = find(node.left)
            maxright = find(node.right)
            max_wout_split = max(max(maxleft,maxright) + node.val,node.val)
            #with split
            ans = max(maxleft + maxright + node.val,ans,max_wout_split)
            return max_wout_split
        find(root)
        return ans