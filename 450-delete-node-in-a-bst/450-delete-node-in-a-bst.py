# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        else: # if key is found
            # the node to be deleted does have only one child
            if not root.left: 
                return root.right
            elif not root.right:
                return root.left
            
            #have both child, find min from right
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            #we have two doubles so we delete root.right
            root.right = self.deleteNode(root.right,root.val)
        return root