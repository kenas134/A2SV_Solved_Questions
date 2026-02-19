
class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))  # convert to strings
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        nums = sorted(nums, key=cmp_to_key(compare))
        
        # handle edge case like [0,0]
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
