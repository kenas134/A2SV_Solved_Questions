class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(start, target, arr):
            if target == 0:
                ans.append(arr[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                arr.append(candidates[i])
                backtrack(i, target - candidates[i], arr)
                arr.pop()

        backtrack(0, target, [])
        return ans