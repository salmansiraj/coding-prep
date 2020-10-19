class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # USE A SET WITH TWO POINTERS (SLIDING WINDOW)
        # removing from a set => set.remove(value)
        # adding value to a set => set.add(value)
        # O(n) time, O(min(m, n))

        substringSet = set()
        start = 0
        end = 0
        currMax = 0

        while (end < len(s)):
            if (s[end] not in substringSet):
                substringSet.add(s[end])
                end += 1
            else:

                substringSet.remove(s[start])
                start += 1

            currMax = max(currMax, len(substringSet))

        return currMax
