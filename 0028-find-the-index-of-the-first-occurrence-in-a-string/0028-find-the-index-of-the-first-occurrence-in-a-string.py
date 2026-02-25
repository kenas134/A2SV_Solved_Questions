class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        for i in range(len(needle)-1,len(haystack)):
            if needle == haystack[left:i+1]:
                return left
            left += 1
        return -1
            