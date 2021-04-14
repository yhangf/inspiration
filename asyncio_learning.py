import time
import asyncio

# 同步模式
def delay():
    time.sleep(1)
    
def main(n):
    for _ in range(n):
        delay()

# 异步模式
async def async_delay():
    await asyncio.sleep(1)
    
async def async_main(n):
    tasks = []
    for _ in range(n):
        tasks.append(
            asyncio.create_task(
                async_delay()
            )
        )
    _ = await asyncio.wait(tasks)
    
    
"""
%%time
main(10)
%%time
asyncio.run(asyncio.sleep(1))
%%time
asyncio.run(async_main(10))
"""
