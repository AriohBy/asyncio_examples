import contextvars
import asyncio

current_language = contextvars.ContextVar("current_language", default="en")


def set_language(language_code):
    current_language.set(language_code)


async def get_greeting():
    language_code = current_language.get()
    greetings = {"en": "Hello!", "ru": "Привет!", "es": "Hola!"}
    return greetings.get(language_code, "Hello!")


async def get_error_message():
    language_code = current_language.get()
    error_messages = {
        "en": "An error occurred.",
        "ru": "Произошла ошибка.",
        "es": "Ocurrió un error.",
    }
    return error_messages.get(language_code, "An error occurred!")


async def test_user_actions(language_code):
    set_language(language_code)
    greeting = await get_greeting()
    print(greeting)
    error_message = await get_error_message()
    print(error_message)


async def main():
    await test_user_actions("en")
    await test_user_actions("ru")
    await test_user_actions("es")


asyncio.run(main())
