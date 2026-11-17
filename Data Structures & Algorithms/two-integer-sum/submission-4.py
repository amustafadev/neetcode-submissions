class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in nums:
                j = nums.index(b)
                if i == j:
                    continue
                return sorted([i, j])