class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r + l) // 2
            val = nums[i]
            if val == target:
                return i
            elif val < target:
                l = i + 1
            else:
                r = i - 1
        return -1