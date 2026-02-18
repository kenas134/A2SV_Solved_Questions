class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(1, n):
            cur_height = heights[i]
            cur_name = names[i]
            j = i - 1
        
            while j >= 0 and heights[j] < cur_height:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = cur_height
            names[j + 1] = cur_name
        return names
            