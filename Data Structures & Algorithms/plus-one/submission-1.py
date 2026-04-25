class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(set(digits)) == 1 and 9 in digits:
            return [1]+[0]*len(digits)
        l = len(digits)-1
        carry = 0
        while l >= 0:
            if l == len(digits)-1:
                sm = digits[l] + 1 + carry
            else:
                sm = digits[l] + carry

            digits[l] = sm % 10
            carry = sm // 10
            l -= 1
            if sm < 10:
                return digits

        return digits
        