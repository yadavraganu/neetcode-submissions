class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_matrix = {}
        no_course_req = {}
        for i in range(numCourses):
            adj_matrix[i] = []
            no_course_req[i] = 0
        for nxt, pre in prerequisites:
            no_course_req[nxt] += 1
            adj_matrix[pre].append(nxt)
        
        res = []
        
        def dfs(node):
            res.append(node)
            no_course_req[node] -= 1
            for n in adj_matrix[node]:
                no_course_req[n] -= 1
                if no_course_req[n] == 0:
                    dfs(n)

        for i in range(numCourses):
            if no_course_req[i] == 0:
                dfs(i)
        print(res)
        return res if len(res) == numCourses else []