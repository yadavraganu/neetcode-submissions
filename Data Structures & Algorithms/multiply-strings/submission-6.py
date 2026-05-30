class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num2)):
            carry = 0
            for j in range(len(num1)):
                res = int(num2[i]) * int(num1[j]) + result[i + j] + carry
                result[i + j] = res % 10
                carry = res // 10
            if carry:
                result[i + len(num1)] += carry

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return "".join(map(str, result[::-1]))
