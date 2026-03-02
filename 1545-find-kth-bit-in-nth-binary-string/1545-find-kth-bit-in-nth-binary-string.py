class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        length = 2**n -1
        def helper(length,k):

            if length == 1:
                return "0"

            half = length//2

            if k > half+1:
                x = helper(half,1+length-k)
                return "0" if x == "1" else "1"
            elif k <= half:
                return helper(half,k)
            else:
                return "1"
        return helper(length,k)

