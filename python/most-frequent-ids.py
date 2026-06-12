class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        maxHeap = []
        result = []
        collection = defaultdict(int)

        for item, count in zip(nums, freq):
            collection[item] += count
            heappush(maxHeap, (-collection[item], item))
            while -maxHeap[0][0] != collection[maxHeap[0][1]]:
                heappop(maxHeap)

            result.append(-maxHeap[0][0])

        return result
