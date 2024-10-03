import asyncio


async def process_task():
    await asyncio.sleep(1)
    current_task = asyncio.current_task()
    return id(current_task)


async def main():
    # Создаем 10 задач, присваивая каждой имя для идентификации
    tasks = [asyncio.create_task(process_task(), name=f"task_{i}") for i in range(10)]
    results = await asyncio.gather(*tasks)
    return results


results = asyncio.run(main())

print(results)
