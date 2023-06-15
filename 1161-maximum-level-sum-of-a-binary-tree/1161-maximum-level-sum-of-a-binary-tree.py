# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        max_level = 1
        q = deque()
        q.append(root)
        cur_level = 0
        while q:
            temp = 0
            for _ in range(len(q)):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur_level += 1
            if temp > max_sum:
                max_sum = temp
                max_level = cur_level
        return max_level