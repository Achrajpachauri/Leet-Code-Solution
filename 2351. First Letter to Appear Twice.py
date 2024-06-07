class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        visit = []

        for i in s:
            if i not in visit:
                visit.append(i)
            
            else:
                return i