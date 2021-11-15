class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cache1 = Counter(nums1)
        self.cache2 = Counter(nums2)
        self.arr2 = nums2

    def add(self, index: int, val: int) -> None:
        if self.cache2[self.arr2[index]] == 1:
            del self.cache2[self.arr2[index]]
        else:
            self.cache2[self.arr2[index]] -= 1

        if self.arr2[index] + val not in self.cache2:
            self.cache2[self.arr2[index] + val] = 1
        else:
            self.cache2[self.arr2[index] + val] += 1

        self.arr2[index] += val

    def count(self, tot: int) -> int:
        result = 0
        for key in self.cache1:
            if tot - key in self.cache2:
                result += self.cache1[key] * self.cache2[tot - key]

        return result
