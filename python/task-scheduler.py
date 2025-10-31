class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        minTime = 0
        freq = [-val for val in Counter(tasks).values()]
        heapify(freq)
        while freq:
            rem = []
            cycle = n + 1
            count = 0
            while cycle and freq:
                top = -heappop(freq)
                if top > 1:
                    rem.append(top - 1)
                cycle -= 1
                count += 1
            for val in rem:
                heappush(freq, -val)
            minTime += n + 1 if freq else count
        return minTime
