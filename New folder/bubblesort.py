
def bubblesort(lst):
    """
    Returns a new sorted list using bubble sort algorithm.
    """
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    # Quick sanity check
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    print("Sorted:  ", bubblesort(data))

