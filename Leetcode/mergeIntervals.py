# In: [[1, 4], [2, 6], [15, 17]]
# Out: [[1, 6], [15, 17]]


def mergeIntervals(intervals):
    intervals.sort(key=lambda elem: elem[0])
    result = [intervals[0]]
    for interval in intervals:
        if interval[0] >= result[-1][0] and interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


def main():
    print(mergeIntervals([[1, 4], [2, 6], [15, 17]]))


main()
