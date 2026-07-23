class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        curr_win = set()
        for r in range(len(nums)):
            
            if nums[r] in curr_win:
                return True 
            
            curr_win.add(nums[r])
            if (r - l) + 1 > k:
                curr_win.remove(nums[l])
                l += 1 
        
        return False
            
