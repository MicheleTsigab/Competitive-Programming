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
        return self.sortedArrayToBST(arr)
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        l = 0
        r = len(nums) - 1
        mid = ceil((l + r)/2)
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root