class Solution:

    def __init__(self, w: List[int]):
        self.indexRanges = [0]
        self.total = 0
        for index in range(0, len(w) - 1):
            self.indexRanges.append(self.indexRanges[-1] + w[index])
            self.total += w[index]
        self.total += w[-1] - 1

    def pickIndex(self) -> int:
        left = 0
        right = len(self.indexRanges) - 1
        index = random.randint(0, self.total)
        while left <= right:
            mid = (left + right) // 2
            if self.indexRanges[mid] > index:
                right = mid - 1
            elif self.indexRanges[mid] < index:
                left = mid + 1
            else:
                return mid

        return left - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
