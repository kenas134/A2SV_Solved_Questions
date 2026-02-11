class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        ans = 0
        last = 0
        for i in s[::-1]:
            if roman[i] >= last:
                ans += roman[i]
                last = roman[i]
            else:
                ans -= roman[i]
        return ans
