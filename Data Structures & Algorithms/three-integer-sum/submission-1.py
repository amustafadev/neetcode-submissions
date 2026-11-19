class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return res

        for i, a in enumerate(nums):
            # no solutuon possible if first (smallest) number is positive
            if a > 0:
                break
            
            # skip if first number same as last iteration (will give same result)
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # make sure left ptr moves to a new value
                    # this ensures no duplicate triples in the
                    # edge case that updated l and r pointers
                    # still give the same triplets
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        # return
        return res
