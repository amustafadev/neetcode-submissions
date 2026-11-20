class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case
        length = len(nums)
        if length == 1:
            return 0 if nums[0] == target else -1
        
        # if rotated find rotation count
        rotation_count = 0
        if nums[0] > nums[-1]:
            l, r = 1, length - 1
            while l <= r:
                i = (l + r) // 2
                if nums[i] < nums[0]:
                    r = i - 1
                else:
                    l = i + 1
            rotation_count = l
        
        # sort and binary search adjusted for rotation
        nums.sort()
        l, r = 0, length - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return (i + rotation_count) % length
            elif nums[i] < target:
                l = i + 1
            else:
                r = i - 1
        
        return -1