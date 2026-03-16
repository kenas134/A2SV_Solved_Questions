class Solution:
    def fib(self, n: int) -> int:
        def rec(n):
            # n is the state
            
            # Base case
            if n == 0:
                return 0
            if n == 1:
                return 1
            # recurence relation
            return rec(n-1) + rec(n-2)
        return rec(n)