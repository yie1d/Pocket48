import asyncio

from aiopocket import Client


async def main():
    async with Client() as client:
        await client.get_starBasicInfo(417321)


async def demo():
    async with Client() as client:
        print(client.user_login())
        print(await client.get_starBasicInfo(417321))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
