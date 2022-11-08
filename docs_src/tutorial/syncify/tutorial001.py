import time

import anyio
from hiya import asyncify, syncify


async def do_async_work(name: str):
    await anyio.sleep(1)
    return f"Hello, {name}"


def do_sync_work(name: str):
    time.sleep(1)
    message = syncify(do_async_work)(name=name)
    return message


async def main():
    message = await asyncify(do_sync_work)(name="World")
    print(message)


anyio.run(main)
