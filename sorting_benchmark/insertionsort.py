

import random
import matplotlib.pyplot as plt
def insertionsort(lst,visualize=True):
    """
    Returns a new sorted list using insertion sort algorithm.
    """
    arr = lst.copy()
    n = len(arr)

    # Visualization setup
    if visualize:
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_xlim(0, n)
        ax.set_ylim(0, max(arr) * 1.1)
        ax.set_title("Insertion Sort")

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if visualize:
                ax.cla()
                ax.bar(range(n), arr, align='edge')
                ax.set_xlim(0, n)
                ax.set_ylim(0, max(lst) * 1.1)
                ax.set_title(f"Insertion Sort (insert key at pos {j+1})")
                plt.pause(0.005)

        arr[j + 1] = key
        if visualize:
            ax.cla()
            ax.bar(range(n), arr, align='edge')
            ax.set_xlim(0, n)
            ax.set_ylim(0, max(lst) * 1.1)
            ax.set_title(f"Insertion Sort (placed key at pos {j+1})")
            plt.pause(0.005)

    if visualize:
        plt.ioff()
        plt.show()    
    return arr


if __name__ == "__main__":
    import random
    data = random.sample(range(100), 10)
    print("Unsorted:", data)
    # Run without visualization
    sorted_plain = insertionsort(data, visualize=False)
    print("Sorted (no viz):", sorted_plain)

    # Run with visualization
    sorted_viz = insertionsort(data, visualize=True)
    print("Sorted (with viz):", sorted_viz)

