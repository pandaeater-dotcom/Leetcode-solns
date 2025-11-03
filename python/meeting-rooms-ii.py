class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key=lambda x: x[0])
        startTimes = [intervals[0][1]]
        for index in range(1, len(intervals)):
            if startTimes[0] <= intervals[index][0]:
                heappop(startTimes)
            heappush(startTimes, intervals[index][1])

        return len(startTimes)
