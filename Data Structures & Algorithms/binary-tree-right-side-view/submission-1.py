# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)

        while q:
            
            nodes_at_lvl = len(q)

            for _ in range(nodes_at_lvl):
                last_node_at_lvl = q.popleft()

                if last_node_at_lvl.left:
                    q.append(last_node_at_lvl.left)
                if last_node_at_lvl.right:
                    q.append(last_node_at_lvl.right)

            res.append(last_node_at_lvl.val)

        return res