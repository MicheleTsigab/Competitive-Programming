# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        parent = dict()
        ans = 0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if node.left.left and node.val % 2==0:
                    ans+=node.left.left.val
                if node.left.right and node.val % 2 ==0:
                    ans+=node.left.right.val
            if node.right:
                q.append(node.right)
                if node.right.right and node.val % 2 == 0:
                    ans+=node.right.right.val
                if node.right.left and node.val % 2 == 0:
                    ans+=node.right.left.val
            
        return ans