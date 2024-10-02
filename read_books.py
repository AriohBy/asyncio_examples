import asyncio


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    students = [("Алекс", 5), ("Мария", 3), ("Иван", 4)]
    tasks = [
        asyncio.create_task(read_book(student, time)) for student, time in students
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
