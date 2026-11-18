import threading
import time

lock = threading.Lock()

def task1():
    with lock:
        print("Task 1: Chopping vegetables")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    with lock:
        print("Task 2: Boiling rice")
    time.sleep(3)
    print("Task 2 completed")

def task3():
    with lock:
        print("Task 3: Making tea")
    time.sleep(1)
    print("Task 3 completed")


# Creating threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Starting threads
start = time.perf_counter()

t1.start()
t2.start()
t3.start()

# Waiting for all threads
t1.join()
t2.join()
t3.join()

end = time.perf_counter()

print("All tasks completed!")
print("Total execution time:", round(end - start, 2), "seconds")