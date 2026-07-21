from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_matrix = defaultdict(list)
        visited= [False]*n
        for a,b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)

        def dfs(node):
            if not visited[node]:
                for neigh in adj_matrix[node]:
                    visited[node] = True 
                    dfs(neigh)
            return
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        return res