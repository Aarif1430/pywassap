import anyio
import hiya


async def do_work(name: str):
    await anyio.sleep(1)
    return f"Hello, {name}"


async def main(name: str):
    result = await do_work(name=name)
    return result


result = hiya.runnify(main)(name="World")
print(result)
