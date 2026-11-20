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

        if timestamp < arr[0][0]:
            return ""
        
        l, r = 0, len(arr) - 1
        while l < r:
            i = (l + r + 1) // 2
            t = arr[i][0]
            if t <= timestamp:
                l = i
            else:
                r = i - 1
        
        return arr[l][1]
