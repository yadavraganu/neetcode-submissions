class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the global maximum result with the first element
        global_max = nums[0]
        
        # Track the local maximum and minimum products ending at the current position
        current_max = nums[0]
        current_min = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            current_num = nums[i]

            # If the current number is negative, it swaps the roles of max and min.
            # A large positive multiplied by a negative becomes a small minimum.
            # A small negative multiplied by a negative becomes a large maximum.
            if current_num < 0:
                current_max, current_min = current_min, current_max

            # The new maximum ending here is either the number itself, 
            # or the product of the number with the previous maximum ending here.
            current_max = max(current_num, current_max * current_num)
            
            # The new minimum ending here is either the number itself,
            # or the product of the number with the previous minimum ending here.
            current_min = min(current_num, current_min * current_num)

            # Update the global maximum encountered across all contiguous subarrays
            global_max = max(global_max, current_max)
            
        return global_max