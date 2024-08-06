import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            else:
                hashmap[num] += 1
        maxheap = []
        for key, value in hashmap.items():
            heapq.heappush(maxheap, (-value, key))

        kmax = []
        for _ in range(k):
            value, key = heapq.heappop(maxheap)
            kmax.append(key)
        
        return kmax
