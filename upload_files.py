import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9,
}

network_speed = 8


async def download_file(file_name, file_size):
    download_time = file_size / network_speed
    print(
        f"Начинается загрузка файла: {file_name}, его размер {file_size} мб, "
        f"время загрузки составит {download_time} сек"
    )
    await asyncio.sleep(download_time)
    print(f"Загрузка завершена: {file_name}")


async def monitor_tasks(tasks):
    while any(not task.done() for task in tasks):
        for task in tasks:
            status = "в процессе" if not task.done() else "завершена"
            print(f"Задача {task.get_name()}: {status}, Статус задачи {task.done()}")
        await asyncio.sleep(1)
    for task in tasks:
        status = "завершена" if task.done() else "в процессе"
        print(f"Задача {task.get_name()}: {status}, Статус задачи {task.done()}")
    print("Все файлы успешно загружены")


async def main():
    tasks = [
        asyncio.create_task(download_file(file_name, file_size), name=file_name)
        for file_name, file_size in files.items()
    ]
    await monitor_tasks(tasks)
    await asyncio.gather(*tasks)


asyncio.run(main())
