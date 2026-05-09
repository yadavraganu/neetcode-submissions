class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        freq_map  = Counter(hand)
        
        if len(hand) % groupSize != 0:
            return False

        count = len(hand) // groupSize
        
        for cnt in range(count):
            start = min(freq_map.keys())
            i = 0
            while i < groupSize:
                if start in freq_map:
                    freq_map[start] -= 1
                    if freq_map[start] == 0:
                        del freq_map[start]
                else:
                    return False
                start += 1
                i += 1
        return True