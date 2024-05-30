class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in words:
            res.append(i.split(separator))

        res1 = [j for i in res for j in i if j !='']

        return res1