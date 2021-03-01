'''
    O(N)
'''


def trap(height: List[int]):
    maxLeft = [0] * len(height)
    maxRight = [0] * len(height)

    for i in range(1, len(height)):
        maxLeft[i] = max(height[i], height[i - 1])

    for i in range(len(height) - 1, -1, -1):
        maxRight = max(height[i], height[i + 1])

    result = 0
    for i in range(len(height)):
        result += min(maxLeft[i], maxRight[i]) - height[i]

    return result
