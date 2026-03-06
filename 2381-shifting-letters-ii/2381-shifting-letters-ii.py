class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pref = [0]*(n+1)

        for i in range(len(shifts)):
            l,r,ss = shifts[i]
            if ss == 1:
                pref[l] += 1
                pref[r+1] -= 1
            else:
                pref[l] -= 1
                pref[r+1] += 1
        ans = []
        for i in range(1,n):
            pref[i] = pref[i] + pref[i-1]

        for i in range(n):
            cur = ord(s[i]) + pref[i] - 97
            cur %= 26

            ans.append(chr(cur+97))

        return "".join(ans)
