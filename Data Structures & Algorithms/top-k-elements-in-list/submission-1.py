class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # calculate frequency
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1 
            else:
                freq[n] = 1

        # sort by frequency
        sort = sorted(freq, key=freq.get, reverse=True)

        # return
        return sort[:k]
