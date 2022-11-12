import concurrent.futures
import time

def func_1(sec):
    for i in range(10):
        print(i*i)
        time.sleep(sec)
    return i


if __name__=='__main__':
    t1=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as exe:
        p1 = exe.submit(func_1, 1)
        p2 = exe.submit(func_1, 1)
        print(p1.result())
        print(p2.result())
    t2=time.perf_counter()
    print(f"Finished in {t2-t1}")