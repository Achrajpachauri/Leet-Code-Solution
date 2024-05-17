class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            m = max(len(i.split()),m)
        
        return m