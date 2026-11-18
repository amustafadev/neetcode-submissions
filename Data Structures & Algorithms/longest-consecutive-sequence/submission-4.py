class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if empty
        if not nums:
            return 0

        # sort unique list
        nums = sorted(list(set(nums)))

        # calculate longest streak
        streak, longest = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                streak = 1
                continue
            streak += 1
            longest = max(streak, longest)
        
        # return
        return longest