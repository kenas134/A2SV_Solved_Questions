class Solution:
    def myPow(self, x: float, n: int) -> float:
        #handle Zero
        if n == 0:
            return 1.0
        
        # handle negative power
        if n < 0:
            x = 1 / x
            n = -n
        #handle positive power
        ans = 1
        while n > 0:
            if n % 2 == 1:     
                ans *= x
            
            x *= x            
            n //= 2            
        
        return ans
