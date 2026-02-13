class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0 for j in range(len(img[0]))]for i in range(len(img))]
        n = len(img)
        m = len(img[0])
        for i in range(len(img)):
            for j in range(len(img[0])):
                summ = 0
                count = 1
                # top
                if i > 0:
                    summ += img[i-1][j]
                    count += 1
                # top left
                if i > 0 and j > 0:
                    summ += img[i-1][j-1]
                    count += 1
                #top right
                if i > 0 and j < m-1:
                    summ += img[i-1][j+1]
                    count += 1
                # bottom
                if i < n-1:
                    summ += img[i+1][j]
                    count += 1
                # bottom left
                if i < n-1 and j > 0:
                    summ += img[i+1][j-1]
                    count += 1
                #bottom right
                if i < n-1 and j < m-1:
                    summ += img[i+1][j+1]
                    count += 1
                #left
                if j > 0:
                    summ += img[i][j-1]
                    count += 1
                if j < m-1:
                    summ += img[i][j+1]
                    count += 1
                summ += img[i][j]
                ans[i][j] = summ//count
        return ans

