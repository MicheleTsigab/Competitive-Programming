# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        q = deque()
        q.append((root,root.val))
        total = 0
        while q:
            node,val = q.popleft()
            
            if node.left:
                q.append((node.left,val*10 + node.left.val))
            if node.right:
                q.append((node.right,val*10 + node.right.val))
            if not node.right and not node.left:
                total += val
        return total