class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        sub_arrays = 0

        for i in range(n):
            for j in range(i,n,2):
                sub_arrays+=sum(arr[i:j+1])

        return sub_arrays