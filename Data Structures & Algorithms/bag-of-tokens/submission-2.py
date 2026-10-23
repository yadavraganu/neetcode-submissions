class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        points = 0
        res = 0
        tokens.sort()
        l = 0
        r = len(tokens)-1
        while l<=r:
            if tokens[l] <= power:
                power -= tokens[l]
                points += 1
                l += 1
                res = max(res,points)
            elif points > 0:
                points -= 1
                power += tokens[r]
                r -= 1
            else:
                break       
        return res



