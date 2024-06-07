from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        c = Counter(s)

        return min(c.values()) == max(c.values())