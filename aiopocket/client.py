import asyncio
from typing import List, Dict, Tuple, Optional, Union

import aiohttp
import toml
from tenacity import retry, stop_after_attempt


class Client:
    def __init__(self) -> None:
        """
        pocket48客户端
        """

        self.__token: Optional[str] = None
        self.__connector: Optional[aiohttp.TCPConnector] = None
        self.__session: Optional[aiohttp.ClientSession] = None

        self.__sem = asyncio.Semaphore(10)
        self.__loop = asyncio.get_running_loop()


    async def __aenter__(self) -> "Client":
        """
        异步上下文管理器 进入时
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        异步上下文管理器 退出时
        """
        pass

    @property
    def connector(self) -> aiohttp.TCPConnector:
        """
        获取TCP连接器

        :return: TCP连接器
        """
        if self.__connector is None:
            self.__connector = aiohttp.TCPConnector(
                ssl=False,
                keepalive_timeout=60,
                limit=0,
                loop=self.__loop,
            )

        return self.__connector

    @property
    def session(self) -> aiohttp.ClientSession:
        """
        用于请求的session
        """
        if self.__session is None:
            time_out = aiohttp.ClientTimeout(total=3)

            self.__session = aiohttp.ClientSession(
                connector=self.connector,
                loop=self.__loop,
                timeout=time_out
            )

        return self.__session

    @property
    def get_headers(self):
        """
        基本headers
        """
        base_headers = {
            aiohttp.hdrs.USER_AGENT: 'PocketFans201807/6.2.0_21061102 (MI 9:Android 7.1.2;Xiaomi Xiaomi-user 7.1.2 20171130.276299 release-keys)',
            aiohttp.hdrs.CONTENT_TYPE: 'application/json; charset=UTF-8',
            aiohttp.hdrs.HOST: 'pocketapi.48.cn',
            aiohttp.hdrs.CONNECTION: 'Connection',
            aiohttp.hdrs.ACCEPT_ENCODING: 'gzip',
            'appInfo': {
                'IMEI': 'fcc6a3c32b4dd4ce',
                'appBuild': '21061102',
                'appVersion': '6.2.0',
                'deviceId': 'fcc6a3c32b4dd4ce',
                'deviceName': 'vmos',
                'osType': 'android',
                'osVersion': '7.1.2',
                'phoneName': 'vmos',
                'phoneSystemVersion': '7.1.2',
                'vendor': 'vmos'
            }
        }

        if self.__token:
            self.update_token()

        return base_headers.update({
            'pa': self.get_pa(),
            'token': self.__token
        })

    async def post(self, url, params):
        async with self.__sem:
            async with self.session.post() as resp:
                # todo 发起请求
                pass

    @staticmethod
    def get_pa():
        # todo 获取pa
        return 'a'

    @staticmethod
    def update_token():
        # todo 更新token
        pass
