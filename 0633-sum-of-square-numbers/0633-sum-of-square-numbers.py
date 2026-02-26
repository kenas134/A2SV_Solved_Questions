class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = isqrt(c) 
        while left <= right:
            cur = right ** 2 + left ** 2
            if cur == c:
                return True
            elif cur > c:
                right -= 1
            else:
                left += 1 
        return False