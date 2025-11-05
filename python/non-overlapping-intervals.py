class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        lastEnd = intervals[0][1]
        removals = 0
        for interval in intervals[1:]:
            if lastEnd <= interval[0]:
                lastEnd = max(lastEnd, interval[1])
                continue
            lastEnd = min(lastEnd, interval[1])
            removals += 1
        return removals
