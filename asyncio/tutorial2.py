import asyncio


async def main():
    print("Uma")
    await foo("Some Text")
    print("Finished")

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("after sleep")

asyncio.run(main())