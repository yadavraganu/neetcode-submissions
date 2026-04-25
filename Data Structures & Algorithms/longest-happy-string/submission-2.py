class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        maxHeap = []
        res = ''
        for count, letter in (a,'a'),(b,'b'),(c,'c'):
            if count > 0:
                heapq.heappush(maxHeap,(-count, letter))
        
        while maxHeap:
            print(res,maxHeap)
            count1 ,letter1 = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1] == res[-2] == letter1:
                if not maxHeap:
                    break
                count2 ,letter2 = heapq.heappop(maxHeap)
                res += letter2
                count2 +=1
                if abs(count2) > 0:
                    heapq.heappush(maxHeap,(count2, letter2))
                heapq.heappush(maxHeap,(count1, letter1))
            else:
                res += letter1
                count1 += 1
                if abs(count1) > 0:
                    heapq.heappush(maxHeap,(count1, letter1))
        return res

        