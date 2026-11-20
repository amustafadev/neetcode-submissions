class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 1, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] < nums[0]:
                r = i - 1
            else:
                l = i + 1

        return nums[l]
