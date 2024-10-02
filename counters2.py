import asyncio

max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}

counters = {"Counter 1": 0, "Counter 2": 0, "Counter 3": 0}

delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}


async def counter(name, delay):
    while counters[name] < max_counts[name]:
        await asyncio.sleep(delay)
        counters[name] += 1
        print(f"{name}: {counters[name]}")


async def main():

    task1 = asyncio.create_task(counter("Counter 1", delays["Counter 1"]))
    task2 = asyncio.create_task(counter("Counter 2", delays["Counter 2"]))
    task3 = asyncio.create_task(counter("Counter 3", delays["Counter 3"]))

    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
