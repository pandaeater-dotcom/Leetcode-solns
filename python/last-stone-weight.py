class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapify(maxHeap)
        while len(maxHeap) > 1:
            first, second = heappop(maxHeap), heappop(maxHeap)
            remWeight = abs(first - second)
            if remWeight:
                heappush(maxHeap, -remWeight)
        return -maxHeap[0] if maxHeap else 0
