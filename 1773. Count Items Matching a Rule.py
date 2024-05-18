class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res =0
        rKey = {'type':0,'color':1,'name':2}
        for i in range(len(items)):
            if ruleValue in items[i] and ruleValue==items[i][rKey[ruleKey]]:
                res+=1
        
        return res