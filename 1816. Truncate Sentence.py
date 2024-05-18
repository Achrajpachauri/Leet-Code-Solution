class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sp = s.split()
        res = []
        for i in range(k):
            res.append(sp[i])

        return ' '.join(res)