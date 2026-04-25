class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= v:
                ix, vl = stack.pop()
                height = vl
                width = i - ix
                area = max(area, height*width)
                start = ix
            stack.append((start,v))
        
        for i, h in stack:
            area = max(area,h * (len(heights)-i))
        
        return area
        