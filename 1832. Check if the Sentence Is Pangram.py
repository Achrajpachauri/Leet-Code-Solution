class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = [0]*26

        for i in sentence:
            count[ord(i)-ord('a')]+=1
        
        for i in count:
            if i == 0:
                return False
        
        return True
