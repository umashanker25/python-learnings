import asyncio
import aiohttp
from aiohttp import ClientSession
import os
import time

urls = ['https://gorest.co.in/public/v2/users', 'https://gorest.co.in/public/v2/posts', 'https://gorest.co.in/public/v2/comments', 'https://gorest.co.in/public/v2/todos']
results = []

def get_tasks(session):
    tasks = []
    for url in urls:
       tasks.append(session.get(url, ssl=False))
        # tasks.append(asyncio.create_task(session.get(url, ssl=False))) // for faster scheduling
    return tasks

async def make_requests():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # responses = await asyncio.gather(*tasks)
        # print(responses)
        for result in asyncio.as_completed(tasks):
         print(await result)


asyncio.run(make_requests())
