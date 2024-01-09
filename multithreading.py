import threading
import time

def compute_task(task_id, duration):
    print(f"Task {task_id} started.")
    time.sleep(duration)  # Simulating a time-consuming task
    print(f"Task {task_id} completed.")

def main():
    threads = []
    number_of_threads = 5  # You can change this to create more or fewer threads

    # Creating and starting threads
    for i in range(number_of_threads):
        thread = threading.Thread(target=compute_task, args=(i, 2))  # Each task takes 2 seconds
        threads.append(thread)
        thread.start()

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
