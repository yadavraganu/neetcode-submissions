from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(crs):
            if visit[crs] == 1:  # cycle detected
                return False
            if visit[crs] == 2:  # already processed
                return True

            visit[crs] = 1  # mark as visiting
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit[crs] = 2  # mark as visited
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
