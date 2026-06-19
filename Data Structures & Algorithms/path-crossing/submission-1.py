class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = (0,0)
        track = set()
        track.add(start)
        for i in path:
            if i == 'N':
                start = (start[0],start[1]+1)
            elif i == 'S':
                start = (start[0],start[1]-1)
            elif i == 'W':
                start = (start[0]-1,start[1])
            elif i == 'E':
                start = (start[0]+1,start[1])
            if start in track:
                return True
            else:
                track.add(start)
        return False