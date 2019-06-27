import threading

def worker(**kwargs):
    """thread worker function"""
    for i in range(10):
        print 'Worker'+str(kwargs['i'])

    return


threads = []
for i in range(10):
    t = threading.Thread(target=worker, kwargs={'i':i})
    threads.append(t)
    t.start()

for i in range(10):
    threads[i].join()
