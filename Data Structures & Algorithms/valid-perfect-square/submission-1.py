class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        
        while start <= end:
            mid = start + ((end-start) // 2)
            square = mid**2
            if square == num:
                return True
            elif num < square:
                end = mid - 1
            else:
                start = mid + 1
        
        return False