class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            w =word.lower()
            if len(set(w+rows[0]))==len(rows[0]) or len(set(w+rows[1]))==len(rows[1]) or len(set(w+rows[2]))==len(rows[2]):
                res.append(word)
        
        return res
