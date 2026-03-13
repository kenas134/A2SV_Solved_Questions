class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxx = 0
        for i in range(len(heights)):
            noww = [i,heights[i]]
            while stack and stack[-1][1] > heights[i]:
                cur = stack.pop()
                maxx = max(cur[1]*(i-cur[0]),maxx)
                noww[0] = cur[0]

            stack.append(noww)

        n = len(heights)
        while stack:
            cur = stack.pop()
            maxx = max(cur[1]*(n-cur[0]),maxx)

        return maxx           




