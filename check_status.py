import asyncio


async def main():
    await asyncio.sleep(0)
    print("Корутина завершена")


def check_loop_status(loop):
    return f"Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}."


loop = asyncio.get_event_loop()

print(check_loop_status(loop))

loop.call_soon(lambda: print(check_loop_status(loop)))
loop.run_until_complete(main())

loop.close()

print(check_loop_status(loop))
