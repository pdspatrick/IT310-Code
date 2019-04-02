import time, random

def timeIt(command, iterations=1):
    # time.time() wasnt working reliably for what I wanted to do.
    start = time.perf_counter_ns()
    for z in range(iterations):
        exec(command)
    stop = time.perf_counter_ns()
    totaltime = (stop - start) / iterations
    return totaltime

def randomishList(min=0, max=500, size=25, seed=1234):
    random.seed=seed
    lst = [random.randint(min,max) for _ in range(size)]
    return lst


