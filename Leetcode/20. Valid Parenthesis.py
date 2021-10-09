def isValid(self, s: str) -> bool:
     dict = {
          '(': ')',
          '[': ']',
            '{': '}'
          }
    bracket = []

    for char in s:s
        if char in dict:
            bracket.append(char)
        else:
            if len(bracket) == 0:
                return False
            if bracket[-1] in dict and dict[bracket[-1]] == char:
                bracket.pop()
            else:
                return False

    if len(bracket) != 0:
        return False
    return True
