from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if nums[i] in d:
                count = count + d[nums[i]]
                d[nums[i]]+=1
            else:
                d[nums[i]]=1

        return count