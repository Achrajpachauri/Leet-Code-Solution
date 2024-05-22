class Solution:
    def replaceDigits(self, s: str) -> str:
        r = list(s)
        for i in range(len(r)):
            if i%2==1:
                r[i] = chr(ord(r[i-1])+int(r[i]))

                
        return ''.join(r)