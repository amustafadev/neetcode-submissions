class Solution:
    def search(self, nums: List[int], target: int) -> int:    
        # find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            i = (l + r) // 2
            if nums[i] > nums[r]:
                l = i + 1
            else:
                r = i
        pivot = l
        
        # binary search in the split target can exist in
        l, r = 0, pivot
        if target <= nums[-1]:
            l, r = pivot, len(nums) - 1

        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
            else:
                r = i - 1
        
        # return
        return -1