class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while True:
            summ = sum(map(lambda x :x**2,map(int,str(n))))
            if summ == 1:
                return True
            if summ in hash_set:
                return False
            hash_set.add(summ)
            n = summ
