class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1,n+1)}
        for i in times:
            adj_list[i[0]].append((i[1],i[2]))
        
        dist = [float('inf')]*(n+1)

        def dfs(node,weight):
            if dist[node] > weight:
                dist[node] = weight
            else:
                return
            if node in adj_list:
                for n, w in adj_list[node]:
                    dfs(n, w + weight)
        dfs(k,0)
        return -1 if max(dist[1:]) == float('inf') else max(dist[1:])
