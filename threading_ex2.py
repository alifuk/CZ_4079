import timeit
def count(_from, _to):
    while _from >= _to:
        _from -= 1

def wo_threading_func():
    count(400000, 200000)
    count(200000, 0)
    #ukázat že to je stejný 4  -> 0

def with_threading_func():
    import threading
    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def with_multiprocessing_func():
    import multiprocessing
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for _ in range(1000):
        pool.apply_async(count, args=(0, 200000))  # ekvivalent Thread().start()
        pool.apply_async(count, args=(400000, 200000))

    pool.close()
    pool.join()

if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading = "with_threading_func()"
    with_multiprocessing = "with_multiprocessing_func()"
    setup = "from __main__ import wo_threading_func, with_threading_func, with_multiprocessing_func"

    #print("Without threads:", timeit.timeit(stmt=wo_threading,
    #                                        setup=setup,
    #                                        number=1000))
    print("With threads:", timeit.timeit(stmt=with_threading,
                                         setup=setup,
                                         number=1000))
    print("With sub-processes:",
          timeit.timeit(stmt=with_multiprocessing,
          setup=setup,
          number=1))