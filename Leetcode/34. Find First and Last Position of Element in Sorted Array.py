class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirstPos(nums, low, high):
            mid = (low + high) // 2
            while (low <= high):
                if nums[mid] == target:
                    if mid - 1 > -1:
                        if nums[mid - 1] == target:
                            return findFirstPos(nums, low, mid - 1)
                        else:
                            return mid
                    else:
                        return mid
                elif nums[mid] > target:
                    return findFirstPos(nums, low, mid - 1)
                else:
                    return findFirstPos(nums, mid + 1, high)
            return -1

        def findLastPos(nums, low, high):
            mid = (low + high) // 2

            while (low <= high):
                if nums[mid] == target:
                    if mid + 1 < len(nums):
                        if nums[mid + 1] == target:
                            return findLastPos(nums, mid + 1, high)
                        else:
                            return mid
                    else:
                        return mid
                elif nums[mid] > target:
                    return findLastPos(nums, low, mid - 1)
                else:
                    return findLastPos(nums, mid + 1, high)
            return -1

        low = 0
        high = len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]

        lowVal = findFirstPos(nums, low, high)
        highVal = findLastPos(nums, low, high)
        return [lowVal, highVal]
