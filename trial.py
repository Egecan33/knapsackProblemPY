def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, start, mid, end):
    left = arr[start : mid + 1]
    right = arr[mid + 1 : end + 1]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def block_sort(arr, block_size):
    n = len(arr)

    for start in range(0, n, block_size):
        end = min(start + block_size - 1, n - 1)
        insertion_sort(arr, start, end)

    while block_size < n:
        for start in range(0, n, 2 * block_size):
            mid = start + block_size - 1
            end = min(start + 2 * block_size - 1, n - 1)
            merge(arr, start, mid, end)
        block_size *= 2


# Example usage:
arr = [5, 2, 9, 4, 7, 6, 1, 3, 8]
block_size = 3
block_sort(arr, block_size)
print(arr)
