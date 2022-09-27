import asyncio

from aiopocket import Client


async def get_text():
    async with Client() as client:
        client.login()


def main():
    loop = asyncio.get_event_loop()
    task = get_text()
    loop.run_until_complete(task)
    loop.close()


if __name__ == '__main__':
     main()