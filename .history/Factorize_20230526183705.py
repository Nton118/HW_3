import logging
from multiprocessing import Process, Manager, cpu_count, Pool
from time import time


def pr_factors(num, m: Manager):
    timer = time()
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    logging.debug(f'Done {time() - timer}')
    m.append(factors)


def factorize_proc(*number): 
    timer = time()
    cores = cpu_count()  
    with Manager() as manager:
        m = manager.list()
        with Pool(cores) as p:
            p.map_async(pr_factors, *number, callback=)
            pr = Process(target=pr_factors, name=f"pr{n}", args=(n, m, ))
            pr.start()
            processes.append(pr)
        
        logging.debug(f'Done in multiprocess mode {time() - timer}')        
        return m

def factorize(*number): 
    timer = time()
    output = []
    for n in number:
        factors = []
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        output.append(factors)
    logging.debug(f'Done in sync mode {time() - timer}')
    return output
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')  
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    a, b, c, d  = factorize_proc(128, 255, 99999, 10651060)


    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


