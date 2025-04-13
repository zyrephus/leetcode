class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        times = self.store.get(key, [])

        if not times:
            return ""
        
        left, right = 0, len(times) - 1

        res = ""

        while left <= right:
            mid = (left + right) // 2

            if times[mid][1] <= timestamp:
                res = times[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
