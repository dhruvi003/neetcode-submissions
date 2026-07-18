class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ls = [1]*n
        prefix = 1 
        for i in range(n):
            ls[i] *= prefix 
            prefix *= nums[i]
        
        suffix = 1 
        for i in range(n-1, -1, -1):
            ls[i] *= suffix
            suffix *= nums[i]
        
        return ls
