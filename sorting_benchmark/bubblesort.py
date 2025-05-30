import random
import matplotlib.pyplot as plt


def bubblesort(lst, visualize=True):

    arr = lst.copy()
    n = len(arr)

    # Visualization setup
    if visualize:
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_xlim(0, n)
        ax.set_ylim(0, max(arr) * 1.1)
        ax.set_title("Bubble Sort")

    # Always perform sorting regardless of visualization
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Update plot if visualizing
                if visualize:
                    ax.cla()
                    ax.bar(range(n), arr, align='edge')
                    ax.set_xlim(0, n)
                    ax.set_ylim(0, max(lst) * 1.1)
                    ax.set_title(f"Bubble Sort (pass {i}, swap at {j})")
                    plt.pause(0.005)

        # Stop if the list is already sorted
        if not swapped:
            break

    # Finalize visualization
    if visualize:
        plt.ioff()
        plt.show()

    return arr


if __name__ == "__main__":
    data = random.sample(range(100), 10)
    print("Unsorted:", data)

    # Run without visualization
    sorted_plain = bubblesort(data, visualize=False)
    print("Sorted (no viz):", sorted_plain)

    # Run with visualization
    sorted_viz = bubblesort(data, visualize=True)
    print("Sorted (with viz):", sorted_viz)
