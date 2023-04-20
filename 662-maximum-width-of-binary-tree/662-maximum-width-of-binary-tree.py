# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        q = deque()
        q.append((root,1))
        
        while q:
            for i in range(len(q)):
                cur,l = q.popleft()
                if cur.left:
                    q.append((cur.left,2*l))
                if cur.right:
                    q.append((cur.right,2*l + 1))
            if len(q) > 1:
                ans = max(ans, q[-1][1] - q[0][1] + 1)
        return ans