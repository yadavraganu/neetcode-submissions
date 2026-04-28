class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_a, len_b = len(str1), len(str2)

        # If there is no common divisor string, this will fail the concatenation test
        if str1 + str2 != str2 + str1:
            return ""

        max_candidate_len = min(len_a, len_b)

        while max_candidate_len > 0:
            candidate = str2[:max_candidate_len]

            repeats_in_a = len_a // max_candidate_len
            repeats_in_b = len_b // max_candidate_len

            if candidate * repeats_in_a == str1 and candidate * repeats_in_b == str2:
                return candidate

            max_candidate_len -= 1

        return ""