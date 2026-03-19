class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def play(n,k):
            if n == 1:
                return 0
            return (play(n-1,k) + k) % n
        return play(n,k) + 1
            