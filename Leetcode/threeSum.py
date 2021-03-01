from collections import defaultdict
from collections import deque

# 3 Sum
''' 
    # O (N ^2) 
    - For N - 2 times we are doing linear work worst case + sorting O(NlogN)
'''


def threeSum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums) - 2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            if nums[i] + nums[start] + nums[end] == 0:
                result.add([nums[i], nums[start], nums[end]])
            elif nums[i] + nums[start] + nums[end] < 0:
                start += 1
            else:
                end += 1
    return result
