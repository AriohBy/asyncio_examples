import asyncio
import random

# Не менять.
random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


# Реализация корутины для проверки новых писем
async def check_mail(server):
    while True:
        result = await server.check_for_new_mail()
        if result == "Ошибка при проверке новых писем.":
            print(result)
            break
        elif result:
            mail = await server.fetch_new_mail()
            print(mail)
        else:
            print("Новых писем нет.")
        await asyncio.sleep(1)  # Опрос проводится каждую секунду


# Реализация корутины main
async def main():
    server = MailServer()
    await check_mail(server)


# Запуск основной корутины
asyncio.run(main())
