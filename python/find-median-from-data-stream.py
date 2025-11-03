class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            heappush(self.minHeap, num)
            return
        elif not self.maxHeap:
            if self.minHeap[0] < num:
                heappush(self.maxHeap, -heappop(self.minHeap))
                heappush(self.minHeap, num)
            else:
                heappush(self.maxHeap, -num)
            return

        if num > self.minHeap[0]:
            heappush(self.minHeap, num)
        elif num < -self.maxHeap[0] or len(self.minHeap) < len(self.maxHeap):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
