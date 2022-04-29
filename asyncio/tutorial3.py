import asyncio


async def main():
    print("Uma")
    task = asyncio.create_task(foo("Some text"))
    await task
    print("Finished")

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())