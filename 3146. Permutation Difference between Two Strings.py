class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = [-1]*26
        res= 0 
        for i in t:
            d[ord(i)-ord('a')] = t.index(i)

        print(d)

        for i in s:
            res+=abs(d[ord(i)-ord('a')]-s.index(i))
        
        return res