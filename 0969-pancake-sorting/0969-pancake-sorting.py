class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        look = len(arr)
        ans = []
        k = len(arr)

        for z in range(len(arr) - 1):
            for i in range(len(arr) - z):
                if arr[i] == look:

                    if i == look - 1:
                        break
                    
                    if i != 0:
                        ans.append(i + 1)
                        arr[:i + 1] = arr[:i + 1][::-1]

                    ans.append(look)
                    arr[:look] = arr[:look][::-1]
                    
                    break
            
            look -= 1

        return ans
