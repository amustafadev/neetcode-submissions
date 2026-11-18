class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init out
        out = [0] * len(nums)

        # check 0s
        if nums.count(0) > 1:
            return out

        # product
        product, zero_index = 1, -1
        for i, n in enumerate(nums):
            if n == 0:
                zero_index = i
                continue
            else:
                product *= n

        # output
        if zero_index > -1:
            out[zero_index] = product
        else:
            for i in range(len(nums)):
                out[i] = product // nums[i]

        # return
        return out
