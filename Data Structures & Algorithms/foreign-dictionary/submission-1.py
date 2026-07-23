class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj_matrix = {chr: set() for word in words for chr in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_matrix[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for i in adj_matrix[node]:
                if dfs(i):
                    return True
            visited[node] = False
            res.append(node)
        for k in adj_matrix.keys():
            if dfs(k):
                return ""
        res.reverse()
        return ''.join(res)