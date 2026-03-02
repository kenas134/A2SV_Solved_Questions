class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(n):
            chk = Counter()
            left = 0
            ans = 0
            for i in range(len(nums)):
                chk[nums[i]] += 1
                while len(chk) > n:
                    chk[nums[left]] -= 1
                    if chk[nums[left]] == 0:
                        del chk[nums[left]]
                    left += 1
                ans += i - left + 1
            return ans
        return count(k)-count(k-1)


        

