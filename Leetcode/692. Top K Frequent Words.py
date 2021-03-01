from collections import Counter


class Solution:
    #     O(N log N)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqMap = Counter(words)
        result = list(freqMap.keys())
        result.sort(key=lambda k: (-freqMap[k], k))

        return result[:k]
