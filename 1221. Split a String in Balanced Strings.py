class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m = c = 0
        for S in s:
            if S == 'L': c += 1
            if S == 'R': c -= 1
            if c == 0: m += 1
        return m