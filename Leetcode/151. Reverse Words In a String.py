def reverseWords(self, s: str) -> str:
    return " ".join(reversed(s.split()))
#         s.strip(' ')
#         result = s.split(' ')
#         ans = []
#         ans = list(filter(lambda val: val != '', result))

#         res = ""
#         for i in range(len(ans) - 1, -1, -1):
#             if i != 0:
#                 res += ans[i] + " "
#             else:
#                 res += ans[i]

#         return res
