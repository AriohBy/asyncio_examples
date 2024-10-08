import asyncio

# Пример данных
log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Запрос на выход", "delay": 2.0},
    {"event": "Ошибка авторизации", "delay": 2.5},
    {"event": "Успешное соединение с БД", "delay": 3.0},
    {"event": "Ошибка соединения с БД", "delay": 3.5},
    {"event": "Запрос к API", "delay": 4.0},
    {"event": "Ошибка запроса к API", "delay": 4.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0},
]


# Асинхронная функция для имитации обработки события
async def fetch_log(event):
    await asyncio.sleep(event["delay"])
    return f"Событие: '{event['event']}' обработано с задержкой {event['delay']} сек."


# Асинхронная функция для обработки всех событий
async def main():
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


# Запуск асинхронной программы
asyncio.run(main())
