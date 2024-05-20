class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        r = ''
        transformation = []

        for i in words:
            for j in i:
                r+=t[ord(j)-ord('a')]
            
            if r not in transformation:
                transformation.append(r)
            
            r=''
        
        return len(transformation)
    
       
