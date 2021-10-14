class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = 0
        stack = []
        currCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                currCount += 1
            elif s[i] == ')':
                maxCount = max(currCount, maxCount)
                stack.pop()
                currCount -= 1

        return maxCount
