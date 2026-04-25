class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax, rmax = height[0], height[-1]
        l, r = 0, len(height)-1
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += abs(lmax - height[l])
            else :
                r -= 1
                rmax = max(rmax, height[r])
                res += abs(rmax - height[r])
        return res