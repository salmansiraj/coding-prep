class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key=lambda elem: elem[0])
        current = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= current[0] and intervals[i][0] < current[1]:
                return False
            else:
                current = [current[0], max(intervals[i][1], current[1])]

        return True
