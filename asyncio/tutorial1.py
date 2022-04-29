import asyncio

# sync and async 
# asyncio is basically allow to run code without waiting for other to finish
# corouitnes - a simple func wrapped with async keyword

async def main():
    print("Uma")


# print(main()) 
# main()
# await main() 
# asyncio.run(main())


# An event loop
loop = asyncio.get_event_loop()
# Pass the co-routine to the loop
result = loop.run_until_complete(main())
print(result) 
loop.stop()