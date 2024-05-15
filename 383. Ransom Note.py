from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        flag = True
        for i in set(ransomNote):
            if i in m and r.get(i) <= m.get(i):
                 flag = True    
            else:
                return False

        return flag
 