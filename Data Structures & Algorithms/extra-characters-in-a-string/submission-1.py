class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert dictionary to a set for fast lookups
        word_set = set(dictionary)
        
        # Memoization dictionary
        memo = {}

        def dfs(start_index: int) -> int:
            # If already computed, return stored result
            if start_index in memo:
                return memo[start_index]

            # Base case: reached the end of the string
            if start_index == len(s):
                return 0

            # Option 1: treat current character as extra
            min_extra = 1 + dfs(start_index + 1)

            # Option 2: try matching dictionary words starting at this index
            for end_index in range(start_index, len(s)):
                substring = s[start_index:end_index + 1]
                if substring in word_set:
                    min_extra = min(min_extra, dfs(end_index + 1))

            # Store result in memo
            memo[start_index] = min_extra
            return min_extra
        
        return dfs(0)