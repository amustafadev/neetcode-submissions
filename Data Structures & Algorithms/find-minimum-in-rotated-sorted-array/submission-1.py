class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        length = len(nums)
        l, r = 1, length - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] < nums[0]:
                r = i - 1
            else:
                l = i + 1

        return nums[l]
