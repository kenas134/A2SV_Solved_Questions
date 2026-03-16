class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        even_sum = 0
        for x in nums:
            if x % 2 == 0:
                even_sum += x

        answer = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            answer.append(even_sum)

        return answer