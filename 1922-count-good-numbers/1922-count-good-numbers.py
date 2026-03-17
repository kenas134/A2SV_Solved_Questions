class Solution:
    def countGoodNumbers(self, n: int) -> int:

        
        even = ceil(n / 2)
        odd = n//2
        return (pow(5,even,pow(10,9) + 7)*pow(4,odd,pow(10,9) + 7))%(pow(10,9) + 7)