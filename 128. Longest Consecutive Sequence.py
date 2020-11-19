class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        longestStreak = 1
        numSet = set(nums)

        for val in nums:
            if val + 1 in numSet:
                currStreak = 1
                currVal = val + 1
                while (currVal in numSet):
                    currVal += 1
                    currStreak += 1

                longestStreak = max(longestStreak, currStreak)

        return longestStreak
