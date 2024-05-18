class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in s:
            if 65<=ord(i)<=90:
                res+=chr(ord(i)+32)
            else:
                res+=i
        
        return res
    
    
## use return s.lower()