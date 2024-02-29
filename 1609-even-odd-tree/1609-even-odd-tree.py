# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        level = 0
        while q:
            x = q[0].val
            if level % 2==0:
                x-=1
            else:
                x+=1
            for i in range(len(q)):
                n = q.popleft()
                if level % 2==0:
                    if n.val % 2 == 0 or n.val <= x:
                   #     print('here',n)
                        return False
                #odd level
                else:
                    if n.val % 2 or n.val >= x:
                    #    print('here odd level',level,n.val,x)
                        return False
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                
                x = n.val
            
            level +=1
        return True