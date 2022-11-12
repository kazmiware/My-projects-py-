import asyncio
import time
import timeit

async def connect():
    for i in range(0,10,2):
        print(i)
        await asyncio.sleep(1)

async def loading():
   for i in range(1,9,2):
       print(i)
       await asyncio.sleep(1)

async def main():
        task_1=asyncio.create_task(connect())
        task_2=asyncio.create_task(loading())
        await task_1
        await task_2

t1=time.perf_counter()
asyncio.run(main())
t2=time.perf_counter()
print(f"Finshed in {t2-t1} seconds")
