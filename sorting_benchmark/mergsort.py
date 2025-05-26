def mergesort(lst):
    """
    Returns a new sorted list using merge sort algorithm.
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return _merge(left, right)


def _merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    # Quick sanity check
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    print("Sorted:  ", mergesort(data))
