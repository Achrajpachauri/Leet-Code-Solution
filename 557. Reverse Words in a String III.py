class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        for i in range(len(res)):
            res[i] = res[i][::-1]
        
        return ' '.join(res)
