class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        from collections import deque
        q = deque()
        res = 0
        for i in range(len(tickets)):
            q.append(i)
        while q:
            res += 1
            j = q.popleft()
            tickets[j] -= 1
            if tickets[j] > 0:
                q.append(j)
            if j == k and tickets[j] == 0:
                return res