class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap or self.hashMap[key] == []:
            return ""
        entries = self.hashMap[key]
        left = 0
        right = len(entries) - 1
        while left <= right:
            mid = left + (right - left) // 2
            curtime, value = entries[mid]

            if curtime > timestamp:
                right = mid - 1
            elif curtime < timestamp:
                left = mid + 1
            else:
                return value

        return entries[right][1] if right > -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
