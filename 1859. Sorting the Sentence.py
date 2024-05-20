class Solution:
    def sortSentence(self, s: str) -> str:
        r = s.split()
        
        res = ['']*len(r)

        for i in range(len(r)):
                res[int(r[i][-1])-1] = r[i][:-1]
        
        return ' '.join(res)