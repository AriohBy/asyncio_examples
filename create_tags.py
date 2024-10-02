import asyncio
import random
from collections import Counter
import json

with open('create_tags.json', 'r', encoding='utf-8') as file:
    articles = json.load(file)


def find_most_common_word(text: str):
    words = text.lower().split()
    counter = Counter(words)
    most_common_word = counter.most_common(1)[0][0]
    return most_common_word


async def download_and_process(article: dict):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    tag = await asyncio.to_thread(find_most_common_word, article["content"])
    article["tag"] = tag


async def main():
    tasks = []
    for article in articles:
        tasks.append(download_and_process(article))
    await asyncio.gather(*tasks)
    for article in articles:
        print(f'{article["title"]}: {article["tag"]}')


asyncio.run(main())
