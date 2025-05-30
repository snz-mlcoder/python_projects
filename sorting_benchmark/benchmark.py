import random
import time

def run_benchmark(algorithms, sizes, num_trials=3):
    """
    Run a simple sequential benchmark on each sorting function.
    
    :param algorithms: dict mapping name → func(lst, **kwargs)
    :param sizes: list of integer sizes to test
    :param num_trials: how many times to repeat each size and take the average
    """
    # Header
    header = ["Size"] + list(algorithms.keys())
    print("{:>8}".format(header[0]), end="")
    for name in header[1:]:
        print("{:>15}".format(name), end="")
    print("\n" + "-" * (8 + 15 * len(algorithms)))

    for n in sizes:
        # Prepare cumulative times for averaging
        total_times = {name: 0.0 for name in algorithms}
        for _ in range(num_trials):
            data = random.sample(range(n * 10), n)
            for name, func in algorithms.items():
                start = time.perf_counter()
                func(data.copy(), visualize=False)  # ensure no viz
                end = time.perf_counter()
                total_times[name] += (end - start)
        # Compute averages
        avg_times = {name: total_times[name] / num_trials for name in algorithms}

        # Print row
        print("{:8d}".format(n), end="")
        for name in algorithms:
            print("{:15.6f}".format(avg_times[name]), end="")
        print()

if __name__ == "__main__":
    from bubblesort import bubblesort
    from insertionsort import insertionsort
    #from selectionsort import selectionsort
    #from mergesort import mergesort
    #from quicksort import quicksort

    algorithms = {
        "BubbleSort": bubblesort,
        "InsertionSort": insertionsort

    }
    sizes = [1000, 5000, 10000]

    run_benchmark(algorithms, sizes)
