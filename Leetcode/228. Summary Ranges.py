class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = []

        start = 0
        end = 0

        while end + 1 < len(nums):
            if (nums[end + 1] != nums[end] + 1):
                if start != end:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    end += 1
                    start = end
                else:
                    result.append(str(nums[end]))
                    start += 1
                    end += 1
            else:
                end += 1

        if start == end:
            result.append(str(nums[end]))
        else:
            result.append(str(nums[start]) + '->' + str(nums[end]))

        return result
