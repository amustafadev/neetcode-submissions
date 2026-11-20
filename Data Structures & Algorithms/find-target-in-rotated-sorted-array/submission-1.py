class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            return 0 if nums[0] == target else -1
        
        min_index = 0
        if nums[0] > nums[-1]:
            l, r = 1, length - 1
            while l <= r:
                i = (l + r) // 2
                if nums[i] < nums[0]:
                    r = i - 1
                else:
                    l = i + 1
            min_index = l
        
        nums.sort()
        l, r = 0, length - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return (i + min_index) % length
            elif nums[i] < target:
                l = i + 1
            else:
                r = i - 1
        
        return -1