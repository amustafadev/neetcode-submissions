class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init out
        out = [0] * len(nums)

        # product
        product, zero_count, zero_index = 1, 0, -1
        for i, n in enumerate(nums):
            if n == 0:
                # check zero count
                zero_count += 1
                if zero_count > 1:
                    return out
                
                # set index of zero and skip
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
