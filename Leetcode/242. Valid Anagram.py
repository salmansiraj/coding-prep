class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dic1:
                dic1[char] += 1
            else:
                dic1[char] = 1

        for char in t:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1

        for key in dic1:
            if key in dic2 and dic1[key] == dic2[key]:
                continue
            else:
                return False

        return True
