class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            if i == i[len(i)-1::-1]:
                return i
        
        return ""