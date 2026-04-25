class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.checkSum(n)
            print(n,visit)
            if n==1:
                return True
        return False 
    def checkSum(self,num):
        op = 0
        while num>0: 
            rem = num % 10
            op += rem*rem
            num = num // 10
        return op        