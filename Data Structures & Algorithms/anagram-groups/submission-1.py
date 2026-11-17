class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # one string
        if len(strs) == 1:
            return [strs]

        # group
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append((s))

        # return
        return list(groups.values())
