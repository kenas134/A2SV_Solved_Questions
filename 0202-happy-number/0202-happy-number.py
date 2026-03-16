class Solution:
    def isHappy(self, n: int) -> bool:
        ans = set()
        ans.add(n)
        while True:
            x = 0
            
            while n:
                x += (n % 10) ** 2
                n = n // 10
            
            if x == 1:
                return True
            elif x in ans:
                return False
            n = x 
            ans.add(x)

 


            