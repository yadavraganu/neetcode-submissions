class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        l = 0
        total_fruits = 0
        res = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total_fruits += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                total_fruits -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            res = max(res,total_fruits)
        return res