class Solution:
    def makesquare(self, matchsticks):
        # Step 1: Check if total length can form a square
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side_length = total // 4

        # Step 2: Sort in descending order (helps prune faster)
        matchsticks.sort(reverse=True)

        # Step 3: Initialize 4 sides of the square
        sides = [0] * 4

        # Recursive function to try placing each matchstick
        def dfs(index):
            # Base case: if we've placed all matchsticks
            if index == len(matchsticks):
                # Check if all sides equal the target length
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length

            # Try to put current matchstick on each side
            for i in range(4):
                # Only place if it doesn't exceed side length
                if sides[i] + matchsticks[index] <= side_length:
                    # Place the stick
                    sides[i] += matchsticks[index]

                    # Recurse to place the next stick
                    if dfs(index + 1):
                        return True  # Found a valid arrangement

                    # Backtrack: remove the stick and try another side
                    sides[i] -= matchsticks[index]

            # If no side worked, return False
            return False

        return dfs(0)