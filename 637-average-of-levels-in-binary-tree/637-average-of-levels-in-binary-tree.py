# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()
        q.append(root)
        ave = []
        while q:
            sums = 0
            cnt = 0
            for _ in range(len(q)):
                n = q.popleft()
                cnt+=1
                sums += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ave.append(sums/cnt)
        return ave