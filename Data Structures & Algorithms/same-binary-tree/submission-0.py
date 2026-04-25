# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False    
        
        if p.val != q.val:
            return False
        else:
            res_start = True    

            res_left = self.isSameTree(p.left,q.left)
            res_right = self.isSameTree(p.right,q.right)
            res =  res_left and res_right
        
        return  res_start and res  


        