class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hash_map = defaultdict(list)

        for i in strs:
            arr = [0]*26
            for j in i: 
                arr[ord(j)-97] += 1
            hash_map[tuple(arr)].append(i)
        return list(hash_map.values())