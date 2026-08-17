from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2  
        
        low, high = 0, len(A)
        
        while low <= high:
            i = (low + high) // 2   # Count of elements taken from A
            j = half - i            # Count of elements taken from B
            
            # Properly check if indices fall below 0 or exceed array length.
            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')
            
            # Check if the partition is correct
            if A_left <= B_right and B_left <= A_right:
                # If total number of elements is odd
                if total % 2 != 0:
                    return float(max(A_left, B_left))
                # If total number of elements is even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
            elif A_left > B_right:
                # Shift partition left in array A
                high = i - 1
            else:
                # Shift partition right in array A
                low = i + 1
                
        return 0.0