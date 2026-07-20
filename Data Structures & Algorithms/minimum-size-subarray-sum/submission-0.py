class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        summ = 0
        min_len = float('inf')

        for j in range(len(nums)):
            summ += nums[j]

            while summ >= target:
                min_len = min(min_len, j-i+1)
                summ -= nums[i]
                i += 1 
            
        return min_len if min_len < float('inf') else 0