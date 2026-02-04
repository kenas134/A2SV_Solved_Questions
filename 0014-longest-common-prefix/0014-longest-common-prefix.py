class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        n = min(len(strs[0]),len(strs[-1]))
        arr = []
        for i in range(n):
            if strs[0][i] == strs[-1][i]:
                arr.append(strs[0][i])
            else:
                break
        return "".join(arr)

        