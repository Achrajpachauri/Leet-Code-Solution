class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0 
        
        for word in words:
            if word[::-1] in words and word!=word[::-1]:
                count+=0.5
            
        return int(count)
