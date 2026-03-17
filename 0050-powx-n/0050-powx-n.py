class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1

            if n % 2 == 0:
                cur =  rec(x,n//2)
                return cur*cur
            if n % 2 == 1:
                cur = rec(x,n//2)
                return x*cur*cur
            
        val = rec(x,abs(n))
        return val if n >= 0 else 1/val
