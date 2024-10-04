import asyncio
import json


# Товары на складе:
with open("warehouse_store.json", "r", encoding="utf-8") as file:
    warehouse_store = json.load(file)
# Заказ:
order = {"Диван": 5, "Обеденный_стол": 3, "Табуретка": 50, "Гардероб": 1}


async def check_store(item, quantity):
    if item in warehouse_store:
        match quantity:
            case _ if quantity > warehouse_store[item]:
                asyncio.current_task().set_name(f'Частично в наличии: {item}')
            case _ if 0 < quantity <= warehouse_store[item]:
                asyncio.current_task().set_name(f'В наличии: {item}')
            case _ if warehouse_store[item] == 0:
                asyncio.current_task().set_name(f'Отсутствует: {item}')
    else:
        asyncio.current_task().set_name(f'Отсутствует: {item}')


async def main():
    tasks = [
        asyncio.create_task(check_store(item, quantity), name="def_name")
        for item, quantity in order.items()
    ]
    await asyncio.gather(*tasks)
    task_names = [task.get_name() for task in tasks]
    sorted_task_names = sorted(task_names)
    for name in sorted_task_names:
        print(name)

asyncio.run(main())
