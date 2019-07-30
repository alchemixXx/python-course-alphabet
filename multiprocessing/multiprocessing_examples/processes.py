import time
from multiprocessing import Process


def print_with_delay(delay, name=None):
    name = str(delay) if name is None else name
    it = 0
    while it <= 50:
        time.sleep(delay)
        it += 1
        print(f"My name is {name}; My delay is {delay}; This is my {i} iteration")


if __name__ == "__main__":
    processes = []
    for i in range(10):
        p = Process(target=print_with_delay, args=(i, ))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        print("Join process")
        print(dir(p))
