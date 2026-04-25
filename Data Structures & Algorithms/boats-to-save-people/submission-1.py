class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        l, r = 0, len(people)-1
        people.sort()
        boat = 0
        
        while l <= r:
            remain = limit - people[r]
            boat += 1
            r -= 1
            if remain >= people[l]:
                l += 1
        return boat 

             


