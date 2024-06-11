class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = ''
        s = ''
        t = ''

        for i in firstWord:
            f+=str(ord(i)-ord('a'))

        for i in secondWord:
            s+=str(ord(i)-ord('a'))
        
        for i in targetWord:
            t+=str(ord(i)-ord('a'))
        
        return (int(f)+int(s)) == int(t)
