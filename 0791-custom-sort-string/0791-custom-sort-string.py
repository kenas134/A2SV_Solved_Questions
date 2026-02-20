class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr = [0]*26
        for i in s:
            n = ord(i)-97
            arr[n] += 1
        ans = []
        for i in range(len(order)):
            cur = ord(order[i])-97
            while arr[cur] > 0:
                ans.append(chr(cur+97))
                arr[cur] -= 1
        for i in range(26):
            while arr[i] > 0:
                ans.append(chr(i+97))
                arr[i] -= 1
        return "".join(ans)
            
                
