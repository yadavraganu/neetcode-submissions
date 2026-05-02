class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p is None or q is None:
            return
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        