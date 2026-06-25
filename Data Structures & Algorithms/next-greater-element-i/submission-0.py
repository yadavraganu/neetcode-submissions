class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater_map = {}
        
        # Stack to keep track of numbers for which we haven't found a next greater yet
        stack = []
        
        # Traverse nums2
        for num in nums2:
            # If current number is greater than the stack's top,
            # it is the "next greater" for that top element
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            stack.append(num)
        
        # For remaining numbers in stack, no next greater exists
        for num in stack:
            next_greater_map[num] = -1
        
        # Build result for nums1 using the map
        return [next_greater_map[num] for num in nums1]
