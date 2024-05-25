class Solution:
    def countPoints(self, rings: str) -> int:
        
        count = ['']*10

        r =list(rings)
        res = 0
        for i in range(len(r)):
            if i%2==1:
                count[int(r[i])]+=r[i-1]
        
        for i in count:
            if 'B' in i and 'G' in i and 'R' in i:
                res+=1

        return res 