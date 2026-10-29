class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(fruits):
            tmp_set = set()
            while r < len(fruits) and (len(tmp_set) < 2 or fruits[r] in tmp_set):
                print(res,r)
                tmp_set.add(fruits[r])
                r += 1
            res = max(res,r-l)
            l += 1
            r = l
        return res

        