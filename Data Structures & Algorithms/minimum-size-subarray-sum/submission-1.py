class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0 
        summ = 0 
        ll = float('inf')

        while r < len(nums):
            summ += nums[r]
            r += 1 

            while summ >= target:
                ll = min(ll,r-l)
                summ -= nums[l]
                l += 1 

            

        return 0 if ll == float('inf') else ll