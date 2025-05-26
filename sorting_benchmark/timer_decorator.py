import time


def timer(func):
    """
    Decorator that measures and prints the execution time of the decorated function.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result

    return wrapper


if __name__ == "__main__":
    # Example usage:
    @timer
    def example(n):
        total = 0
        for i in range(n):
            total += i
        return total

    example(1000000)
