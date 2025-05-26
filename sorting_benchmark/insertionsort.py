def insertionsort(lst):
    """
    Returns a new sorted list using insertion sort algorithm.
    """
    arr = lst.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    print("Sorted:  ", insertionsort(data))
