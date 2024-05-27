class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        right_sum = []
        res = []
        
        right_sum = [sum(nums[i+1:]) for i in range(len(nums))]

        left_sum = [sum(nums[:-i]) for i in range(len(nums),0,-1)]

        res = [abs(left_sum[i]-right_sum[i]) for i in range(len(nums))]

                
        return res