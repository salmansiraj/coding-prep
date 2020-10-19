class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals) == 0 or len(intervals) == 0):
            return intervals
        result = []

        intervals.sort()

        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= currInterval[1]:
                currInterval[1] = max(currInterval[1], intervals[i][1])

            else:
                result.append(currInterval)
                currInterval = intervals[i]

        result.append(currInterval)
        return result
