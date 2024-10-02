import asyncio
import contextvars

order_state = contextvars.ContextVar("empty_state")


def set_order_state(state):
    order_state.set(state)


async def process_order(order_id):
    set_order_state("Принят")
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")
    await asyncio.sleep(1)

    set_order_state("Обрабатывается")
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")
    await asyncio.sleep(1)

    set_order_state("Отправлен")
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")
    await asyncio.sleep(1)


async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    tasks = []

    for order_id in orders:
        tasks.append(process_order(order_id))
    await asyncio.gather(*tasks)


asyncio.run(main())
