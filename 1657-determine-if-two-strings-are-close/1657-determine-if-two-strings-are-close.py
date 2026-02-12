class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not set(word1) == set(word2):
            return False
        count = Counter(word1)
        count2 = Counter(word2)

        v1 = list(count.values())
        v2 = list(count2.values())
        v1.sort()
        v2.sort()
        if v1 == v2:
            return True
        else:
            return False