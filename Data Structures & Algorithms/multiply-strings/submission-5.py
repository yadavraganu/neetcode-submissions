class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        result = [0]*(len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num2)>len(num1):
            num1 , num2 = num2, num1
        for i in range(len(num2)):
            carry = 0
            for j in range(len(num1)):
                m = int(num2[i])
                n = int(num1[j])
                res = (m*n)+ carry + result[i+j]
                digit = res % 10
                carry = res // 10
                result[i+j] = digit
            if carry:
                result[i+j+1] = carry
            print(result)
        last_zero = len(result)
        for k in range(len(result)-1,-1,-1):
            if result[k] != 0:
                last_zero = k+1
                break
        result = list(map(str,result[0:last_zero]))
        return ''.join(result[::-1])