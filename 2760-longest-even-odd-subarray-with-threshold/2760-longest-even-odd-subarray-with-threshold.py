class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        max_length = 0
        i = 0
        
        while i < n:
            # Skip invalid starting positions
            while i < n and (nums[i] % 2 != 0 or nums[i] > threshold):
                i += 1
            
            if i >= n:
                break
            
            start = i
            length = 1
            
            # Expand the window
            while i + length < n:
                curr_idx = start + length
                prev_idx = curr_idx - 1
                
                if nums[curr_idx] > threshold:
                    break
                
                # Check if parity alternates
                if (nums[prev_idx] % 2) != (nums[curr_idx] % 2):
                    length += 1
                else:
                    break
            
            max_length = max(max_length, length)
            i = start + 1
        
        return max_length