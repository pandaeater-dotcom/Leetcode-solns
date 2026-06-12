class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        days = range(events[0][0], max(end for start, end in events) + 1)
        attended = 0
        minheap = []
        index = 0

        for day in days:
            while index < len(events) and day == events[index][0]:
                heappush(minheap, events[index][1])
                index += 1

            while minheap and minheap[0] < day:
                heappop(minheap)

            if minheap:
                heappop(minheap)
                attended += 1

        return attended
