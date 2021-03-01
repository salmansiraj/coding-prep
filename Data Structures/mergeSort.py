
'''
O(nlogn )
 This is because the list is being split in log(n) calls and the merging process takes linear time in each call.
'''


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid + 1:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while (i < len(arr) and j < len(arr)):
            if arr[i] <= arr[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1

        while i < len(arr):
            arr[k] = arr[i]
            i += 1
            k += 1

        while j < len(arr):
            arr[k] = arr[j]
            j += 1
            k += 1
