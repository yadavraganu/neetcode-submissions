class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def _helper(i,j,a_scr,b_scr):
            alice = True
            if i > j:
                return a_scr, b_scr
            if alice:
                if piles[i]>=piles[j]:
                    a_scr += piles[i]
                    _helper(i+1,j,a_scr,b_scr)
                    alice = False

                else:
                    a_scr += piles[j]
                    _helper(i,j-1,a_scr,b_scr)
                    alice = False
            else:
                if piles[i]>=piles[j]:
                    b_scr += piles[i]
                    _helper(i+1,j,a_scr,b_scr)
                    alice = True

                else:
                    b_scr += piles[j]
                    _helper(i,j-1,a_scr,b_scr)
                    alice = True
            return a_scr, b_scr
        a_scr, b_scr = _helper(0,len(piles)-1,0,0)
        return a_scr > b_scr
