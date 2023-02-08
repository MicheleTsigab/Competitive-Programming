class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skill_sum = 0
        l,r = 0, len(skill) - 1
        result = 0
        while l < r:
            if not skill_sum:
                skill_sum = skill[r] + skill[l]
            elif skill[r] + skill[l] != skill_sum:
                return -1
            result += skill[r] * skill[l]
            l+=1
            r-=1
        return result