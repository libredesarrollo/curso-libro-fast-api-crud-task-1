import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def taskAsync(text = 'Message'):
    while(True):
        print(text)
        await asyncio.sleep(1)

try:
    asyncio.ensure_future(taskAsync())
    asyncio.ensure_future(taskAsync("Other Message"))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()