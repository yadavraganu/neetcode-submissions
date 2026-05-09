from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq_map = Counter(hand)
        for card in sorted(freq_map):  # iterate in ascending order
            while freq_map[card] > 0:
                for i in range(groupSize):
                    next_card = card + i
                    if freq_map[next_card] <= 0:
                        return False
                    freq_map[next_card] -= 1
        return True
