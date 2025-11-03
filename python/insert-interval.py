class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        modifiedIntervals = []
        index = 0
        num = len(intervals)
        while index < num and newInterval[0] > intervals[index][1]:
            modifiedIntervals.append(intervals[index])
            index += 1

        while index < num and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        modifiedIntervals.append(newInterval)

        while index < num:
            modifiedIntervals.append(intervals[index])
            index += 1

        return modifiedIntervals
