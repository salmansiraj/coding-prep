# Merge two sorted lists
'''
    O (len(arr1) + len(arr2))
'''


def mergeLists(arr1, arr2):
    ptr1 = ptr2 = resPtr = 0
    result = [0] * (len(arr1) + len(arr2))
    while (ptr1 < len(arr1) and ptr2 < len(ptr2)):
        if arr1[ptr1] >= arr2[ptr2]:
            result[resPtr] = arr2[ptr2]
            ptr2 += 1
        else:
            result[resPtr] = arr2[ptr2]
            ptr1 += 1
        resPtr += 1

    if ptr1 < len(arr1):
        for i in range(ptr1, len(arr1)):
            result[resPtr] = arr1[i]
            resPtr += 1

    if ptr2 < len(arr2):
        for i in range(ptr2, len(arr2)):
            result[resPtr] = arr2[i]
            resPtr += 1

    return result
