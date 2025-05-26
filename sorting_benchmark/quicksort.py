
def quicksort(lst):
    """
    Returns a new sorted list using quick sort algorithm.
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    # Quick sanity check
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    print("Sorted:  ", quicksort(data))

