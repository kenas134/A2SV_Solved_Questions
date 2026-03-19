class Solution:
    def lastRemaining(self, n: int) -> int:
        def play(n, direction):
            if n == 1:
                return 1
            
            if direction == 0:  
                return 2 * play(n // 2, 1)
            else:
                if n % 2 == 1:
                    return 2 * play(n // 2, 0)
                else:
                    return 2 * play(n // 2, 0) - 1
        
        return play(n, 0)