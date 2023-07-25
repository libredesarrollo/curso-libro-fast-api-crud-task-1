import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def taskAsync(text = 'Message'):
    print(text)

try:
    print('antes de la tarea')
    loop.run_until_complete(taskAsync())
    loop.run_forever()
    print('despues de la tarea')
except KeyboardInterrupt:
    pass
finally:
    loop.close()