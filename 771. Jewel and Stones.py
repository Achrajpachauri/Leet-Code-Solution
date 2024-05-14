class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        for i in range(len(stones)):
            if stones[i] in d:
                d[stones[i]]+=1
            else:
                d[stones[i]]=1

        count = 0

        for i in jewels:
            if i in  d:
                count+=d[i]

        return count