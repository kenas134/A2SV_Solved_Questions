class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = [points[0]]
        
        l = points[0][0]
        r = points[0][1]
        arrow = 1
        for i in range(1,len(points)):
            start,end = points[i][0],points[i][1]
            if start <= r:
                l = max(start,l)
                r = min(end,r)
            else:
                arrow += 1
                l = start
                r = end
        return arrow

