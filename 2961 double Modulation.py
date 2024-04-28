class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        l = []
        for i in range(len(variables)):
            k = ((variables[i][0]**variables[i][1] % 10)**variables[i][2]) % variables[i][3]

            if k == target:
                l.append(i)
        
        return l
        