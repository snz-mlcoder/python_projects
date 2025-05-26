
def selectionsort(lst):
    """
    Returns a new sorted list using selection sort algorithm.
    """
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    print("Sorted:  ", selectionsort(data))

