import threading
import math

def is_divisible(n, start, end, found_divisor, stop_computation, thread_id):
    """
    Checks if 'n' is divisible by any number in the range 'start' to 'end'.
    If a divisor is found, sets 'found_divisor' event, 'stop_computation' flag, and prints the thread ID.
    """
    for i in range(start, end):
        if stop_computation.is_set():
            return
        if n % i == 0:
            found_divisor.set()
            stop_computation.set()
            print(f"Divisor found by thread {thread_id}: {i}")
            return
    print(f"Thread {thread_id}: No divisor found in range {start}-{end - 1}")

def is_prime(n, num_threads=4):
    """
    Determines if 'n' is a prime number using 'num_threads' threads.
    """
    if n <= 2:
        return n == 2

    found_divisor = threading.Event()
    stop_computation = threading.Event()
    threads = []
    sqrt_n = int(math.sqrt(n)) + 1
    interval = (sqrt_n - 2) // num_threads

    for i in range(num_threads):
        start = i * interval + 2
        end = start + interval
        if i == num_threads - 1:  # Adjust the end for the last thread
            end = sqrt_n

        thread_id = i
        thread = threading.Thread(target=is_divisible, args=(n, start, end, found_divisor, stop_computation, thread_id))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return not found_divisor.is_set()

# Example usage
n = 289
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
