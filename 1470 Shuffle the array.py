class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        count = n
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[count])
            count+=1
        
        return ans 
