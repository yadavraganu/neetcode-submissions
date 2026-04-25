# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):

            if not root:
                return 0
            
            height_l = height(root.left)
            height_r = height(root.right)

            return max(height_l,height_r)+1

        if not root:
            return True
        
        l_h = height(root.left)
        r_h = height(root.right)
        
        if abs(l_h - r_h) > 1:
            return False 

        l_b = self.isBalanced(root.left)
        r_b = self.isBalanced(root.right)

        return l_b and r_b
      