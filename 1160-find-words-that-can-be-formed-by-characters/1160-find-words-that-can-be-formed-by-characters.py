class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=0
        h = Counter(chars)

        for word in words:
            valid=True
            for i in word:
                if i not in h or h[i]<word.count(i):
                    valid=False
                    break
            if valid:
                c+=len(word)
        return c