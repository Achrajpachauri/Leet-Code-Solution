class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        from numpy import sort

        d = defaultdict(int)
        temp = sort(nums)
        res = []

        for i in range(len(temp)):
            if temp[i] not in d:
                d[temp[i]]+=i

        for i in range(len(nums)):
            res.append(d[nums[i]])


        return res