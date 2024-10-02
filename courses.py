import asyncio


async def study_course(student, course, steps, speed):
    reading_time = round(steps / speed, 2)
    print(f"{student} начал проходить курс {course}.")
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {reading_time} ч.")


async def main():
    students = {
        "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
        "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
        "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57},
    }

    tasks = [
        asyncio.create_task(
            study_course(student, data["course"], data["steps"], data["speed"])
        )
        for student, data in students.items()
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())
