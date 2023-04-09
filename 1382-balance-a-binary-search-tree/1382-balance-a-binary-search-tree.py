# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.sortedArrayToBST(arr,l = 0, r = len(arr) -1)
        
    def sortedArrayToBST(self, nums, l,r):
        
        if l > r:
            return None
        mid = ceil((l + r)/2)
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums,l,mid - 1)
        root.right = self.sortedArrayToBST(nums,mid + 1,r)
        return root