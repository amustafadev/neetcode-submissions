class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashMap.get(key)
        if not arr:
            return ""
        
        res = ""
        for (ts, val) in arr:
            if ts > timestamp:
                break
            res = val
        
        return res
