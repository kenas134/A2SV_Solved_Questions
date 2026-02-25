class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        i = 0
        j = len(skill)-1
        cur = skill[0]+skill[-1]
        while i < j:
            if skill[i] + skill[j] == cur:
                ans += (skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                return -1
        return ans
        
