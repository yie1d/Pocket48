import asyncio

from aiopocket import Client


# https://source.48.cn/
async def main():
    async with Client() as client:
        # 农燕萍   417321
        # m = await client.get_userInfo(417321)
        # await client.get_starBasicInfo()
        # await client.get_starBasicInfo(417321)
        await client.get_roomInfo(63554)


async def demo():
    async with Client() as client:
        # print(client.user_login())
        print(await client.get_starBasicInfo(417321))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
