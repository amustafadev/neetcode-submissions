class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # calculate frequency
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        # sort by frequency
        return sorted(freq, key=freq.get, reverse=True)[:k]
