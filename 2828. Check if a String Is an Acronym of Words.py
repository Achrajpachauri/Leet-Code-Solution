class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        if len(words)!=len(s):
            return False
        ans =''
        
        for w in words:
            ans+=w[:1]

        return s==ans
         