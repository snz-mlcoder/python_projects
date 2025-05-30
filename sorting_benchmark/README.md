## Benchmark Suite

This project includes a benchmarking script (`benchmark.py`) that runs five sorting algorithms  
(MergeSort, QuickSort, BubbleSort, InsertionSort, SelectionSort) on three data sizes (1,000; 5,000; 10,000)  
and compares their execution times in both **Sequential** and **Parallel** modes.


## Visualization

Both BubbleSort and InsertionSort support optional step-by-step animation:

```python
from bubblesort import bubblesort
sorted_list = bubblesort(data, visualize=False)  # no animation

sorted_list = bubblesort(data, visualize=True)   # with animation


### How to run

```bash
python benchmark.py
