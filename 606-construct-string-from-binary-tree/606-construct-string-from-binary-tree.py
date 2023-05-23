# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(str(node.val))
            if not node.left and not node.right:
                return
            ans.append('(')
            dfs(node.left)
            ans.append(')')
            if node.right:
                ans.append('(')
                dfs(node.right)
                ans.append(')')
            
        dfs(root) 
        x = []  
    #  print(ans)
        for i in range(len(ans)):
            if ans[i] == '(' and ans[i+1]==')':
                continue
            if ans[i]==')' and ans[i-1]=='(':
                continue
            x.append(ans[i])
        return ''.join(ans)