class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        wdw = sum([1 if i == 'W' else 0 for i in blocks[0:k]])
        res = wdw
        for i in range(0,len(blocks)-k):
            if blocks[i] == 'W':
                wdw -= 1
            if blocks[i+k] == 'W':
                wdw += 1
            res = min(res,wdw)
        return res


        