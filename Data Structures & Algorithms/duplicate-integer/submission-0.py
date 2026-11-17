class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for n in nums:
            if d.get(n, 0) > 0:
                return True
            d[n] = 1
        return False 