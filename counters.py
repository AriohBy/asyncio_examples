import asyncio

max_counts = {"Counter 1": 13, "Counter 2": 7}

counters = {"Counter 1": 0, "Counter 2": 0}


async def counter(name, delay):
    while counters[name] < max_counts[name]:
        await asyncio.sleep(delay)
        counters[name] += 1
        print(f"{name}: {counters[name]}")


async def main():
    task1 = asyncio.create_task(counter("Counter 1", 1))
    task2 = asyncio.create_task(counter("Counter 2", 1))
    await asyncio.gather(task1, task2)


asyncio.run(main())
