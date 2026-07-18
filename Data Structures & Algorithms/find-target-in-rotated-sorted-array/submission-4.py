class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Find pivot (minimum element)
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_i = l

        # Choose search range
        if min_i == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, len(nums) - 1

        # Standard binary search
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1