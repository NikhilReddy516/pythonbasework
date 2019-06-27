import threading
from threading import Lock


arr = [i for i in range(0, 100)]
lock = Lock()
globalSum = 0


def sumArr(start , end):
    for index in range(start, end):
        lock.acquire()
        global globalSum
        globalSum = globalSum+arr[index]
        lock.release()


if __name__ == "__main__":
    start = 0
    end = 10
    threads = []
    for i in range(10):
        t = threading.Thread(target=sumArr, kwargs={'start':start, 'end' : end})
        start = end
        end = end+10
        threads.append(t)
        t.start()

    for i in range(10):
        threads[i].join()

    print(globalSum)
