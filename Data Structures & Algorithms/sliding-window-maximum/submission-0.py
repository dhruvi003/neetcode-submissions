class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        lst = []
        for i in range(len(nums)-k+1):
            current_window = nums[i:i+k]
            lst.append(max(current_window))
        return lst