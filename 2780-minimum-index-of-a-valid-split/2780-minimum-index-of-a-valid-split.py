class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count1 = Counter(nums)
        count2 = Counter()
        for i in range(len(nums)):
            left = (i + 1)//2
            right = (len(nums)-i-1)//2
            count1[nums[i]] -= 1
            count2[nums[i]] += 1
            if count1[nums[i]] > right and count2[nums[i]] > left:
                return i
        return -1
