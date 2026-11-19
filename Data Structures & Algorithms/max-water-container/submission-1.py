class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxim = 0
        l, r = 0, len(heights) - 1

        while l < r:
            cur = min(heights[l], heights[r]) * (r - l)
            maxim = max(cur, maxim)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxim