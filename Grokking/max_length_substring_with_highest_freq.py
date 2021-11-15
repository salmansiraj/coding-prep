def maxFreq(s):
    freqDict = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] in freqDict:
                freqDict[s[i:j + 1]] += 1
            else:
                freqDict[s[i:j + 1]] = 1

    maxFreq = 0
    maxStr = ''

    for key in freqDict:
        if freqDict[key] > maxFreq:
            maxFreq = freqDict[key]
            maxStr = key
        elif freqDict[key] == maxFreq:
            maxStr = max(len(key), len(maxStr))

    return maxFreq
