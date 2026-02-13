class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        print(arr)
        chk = {}
        chk2 = {}
        if len(arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if arr[i] not in chk and   pattern[i] in chk2 or arr[i] not in chk and  pattern[i] in chk2:
                return False
            elif arr[i] in chk or pattern[i] in chk2:
                if pattern[i] != chk[arr[i]] or arr[i] != chk2[pattern[i]]:
                    return False
            else:
                chk[arr[i]] = pattern[i]
                chk2[pattern[i]] = arr[i]
        return True
