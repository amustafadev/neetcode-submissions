class Solution:
    dlm = "%S%"

    def encode(self, strs: List[str]) -> str:
        out = self.dlm
        for s in strs:
            out += s + self.dlm
        return out

    def decode(self, s: str) -> List[str]:
        return s.split(self.dlm)[1:-1]
