class Solution:
    def countGoodNumbers(self, n: int) -> int:

        
        even = ceil(n / 2)
        odd = n//2
        return pow(5,even,1000000007)*pow(4,odd,1000000007)%1000000007