from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its time to reach the target
        cars = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)
        
        fleets = 0
        max_time = 0
        
        for _, time in cars:
            if time > max_time:
                fleets += 1
                max_time = time  # This car starts a new fleet
        
        return fleets