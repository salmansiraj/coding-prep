class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 0 or (k > len(s)):
            return s

        stack = []

        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1

            else:
                stack.append([c, 1])

            if stack[-1][1] >= k:
                stack.pop()

        if stack:
            result = ""
            for c, n in stack:
                result += c * n

            return result

        return s
