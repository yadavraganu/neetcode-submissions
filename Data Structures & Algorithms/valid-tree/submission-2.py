class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        if len(edges) != n - 1:
            return False
        adj_matrix = defaultdict(list)
        for u, v in edges:
            adj_matrix[u].append(v)
            adj_matrix[v].append(u)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)    
            for neigh in adj_matrix[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh,node):
                    return False
            return True
        return dfs(0,-1) and len(visited)== n
