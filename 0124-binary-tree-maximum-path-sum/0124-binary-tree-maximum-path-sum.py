# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #ans = -inf
        
        
        def find(node):
            """
            returns max sum without split for each node
            while also updating the global variable with the max sum with splitting
            """
        #    nonlocal ans
            if not node:
                return [0,-inf]
            maxleft = find(node.left)
            maxright = find(node.right)
            ans = max(maxleft[1],maxright[1])
            max_wout_split = max(max(maxleft[0],maxright[0]) + node.val,node.val)
            #with split
            max_with_split = maxleft[0] + maxright[0] + node.val
            ans = max(max_with_split,ans,max_wout_split)
            return [max_wout_split,ans]
        return max(find(root))
        