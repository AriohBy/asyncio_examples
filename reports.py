import asyncio
import json

with open("reports.json", "r", encoding="utf-8") as file:
    reports = json.load(file)


async def download_data(report: dict):
    report_name = report["report"]
    name = report["name"]
    if name == "Дмитрий Орлов":
        task_for_cancel = asyncio.current_task()
        await cancel_task(task_for_cancel)
        print(
            f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные"
        )
        return
    await asyncio.sleep(report["load_time"])
    print(f"Отчет: {report_name} для пользователя {name} готов")


async def cancel_task(task):
    task.cancel()


async def main():
    tasks = [
        asyncio.create_task(download_data(report), name=f"task_{report['report']}")
        for report in reports
    ]
    for task in tasks:
        try:
            await task
        except asyncio.CancelledError:
            pass

asyncio.run(main())
