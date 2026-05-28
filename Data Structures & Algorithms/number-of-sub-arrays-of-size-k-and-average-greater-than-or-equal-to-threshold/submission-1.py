class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        init_sum = sum(arr[0:k])
        res = [init_sum/k] if (init_sum/k) >= threshold else []
        for i in range(k,len(arr)):
            updated_sum = init_sum + arr[i] - arr[i-k]
            updated_avg = updated_sum/k
            if updated_avg >=threshold:
                res.append(updated_avg)
            init_sum = updated_sum
        return len(res)

        