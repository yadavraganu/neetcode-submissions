class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            max_elem = i[-1]
            if target <= max_elem:
                l, r = 0 ,len(i)-1

                while l <= r:
                    m = (l+r)//2
                    if i[m] == target:
                        return True
                    elif i[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
        return False     
        