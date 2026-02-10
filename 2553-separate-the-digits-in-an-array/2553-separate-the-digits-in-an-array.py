class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = list(map(str,nums))
        s2 = "".join(s)
        return list(map(int,list(s2)))