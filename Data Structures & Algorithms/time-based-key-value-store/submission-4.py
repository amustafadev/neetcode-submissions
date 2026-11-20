class TimeMap:

    # BINARY SEARCH INTUITION
    #
    # 1. Always maintain an invariant: what do l and r represent,
    #    and where is the answer guaranteed to be?
    #
    # 2. while l < r:
    #    - Narrow down to ONE guaranteed candidate (l == r).
    #    - Keep possible answers in the search space.
    #    - No final check needed if the invariant guarantees correctness.
    #    - If r = m, use m = (l + r) // 2 (round DOWN).
    #    - If l = m, use m = (l + r + 1) // 2 (round UP).
    #
    # 3. while l <= r:
    #    - Search until NO unchecked candidates remain (l > r).
    #    - Even when l == r, the final candidate still needs checking.
    #    - Use l = m + 1 or r = m - 1 to eliminate inspected indices.
    #    - Save valid candidates separately (res) if needed.
    #
    # 4. WHY MIDPOINT ROUNDING MATTERS:
    #    - Round down guarantees l <= m < r (when l < r).
    #    - Round up guarantees l < m <= r (when l < r).
    #    - Every iteration MUST shrink the search space.
    #
    # 5. BEFORE WRITING CODE, ASK:
    #    - Which elements can I safely eliminate?
    #    - Could m itself be the answer? If so, where do I preserve it?
    #    - Does every pointer update guarantee progress?
    #    - When the loop ends, is the answer already known or must I check it?

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        arr = self.hashMap.get(key, [])
    
        l, r = 0, len(arr) - 1
        while l <= r:
            i = (l + r) // 2
            if arr[i][0] <= timestamp:
                res = arr[i][1]
                l = i + 1
            else:
                r = i - 1
        
        return res
