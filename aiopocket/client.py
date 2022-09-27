import asyncio
import os
import json

from uuid import uuid1
from time import time
from hashlib import md5
from base64 import b64encode
from typing import List, Dict, Tuple, Optional, Union
from pprint import pprint

import aiohttp
import toml
import yarl
import requests
from tenacity import retry as aretry, stop_after_attempt
from retrying import retry

from .typedefs import LoginUserInfo


class Client:
    def __init__(self) -> None:
        """
        pocket48客户端
        """
        self.__config: Optional[dict] = None

        self.__uuid: Optional[str] = str(uuid1()).replace('-', '')
        self.__login_user: Optional[LoginUserInfo] = None
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
    def config(self):
        """
        配置项
        """
        if self.__config is None:
            with open('config.toml', 'r') as f:
                self.__config = toml.load(f)

        return self.__config

    @property
    def get_headers(self):
        """
        基本headers
        """
        base_headers = {
            aiohttp.hdrs.USER_AGENT: self.config['Headers']['user_agent'],
            aiohttp.hdrs.CONTENT_TYPE: self.config['Headers']['content_type'],
            aiohttp.hdrs.HOST: self.config['Headers']['host'],
            aiohttp.hdrs.CONNECTION: 'close',
            aiohttp.hdrs.ACCEPT_ENCODING: self.config['Headers']['content_type'],
            'appInfo': self.config['Headers']['appInfo']
        }

        if self.__login_user.token is None:
            self.login()

        return base_headers.update({
            'pa': self.get_pa(),
            'token': self.__login_user.token
        })

    async def apost(self, _url, _params, _headers=None):
        async with self.__sem:
            async with self.session.post() as resp:
                # todo 发起请求
                pass

    @staticmethod
    @retry(stop_max_attempt_number=3, wait_fixed=3)
    def rpost(_url: yarl.URL, _params: Dict[str, str], _headers: Optional[Dict[str, str]] = None,
              _timeout: int = 3) -> dict:
        """
        发起普通post请求
        """
        res_json = requests.post(
            url=str(_url),
            json=_params,
            headers=_headers,
            timeout=_timeout
        ).json()

        return res_json

    def get_pa(self) -> str:
        """
        获取pa值
        """
        _PostKey = self.config['paInfo']['PostKey']
        _PostKeyVersion = self.config['paInfo']['PostKeyVersion']
        _UUID = self.__uuid
        _NOW_TIME = str(int(time() * 1000))
        _MD5 = md5((_NOW_TIME + _UUID + _PostKey).encode()).hexdigest()

        return b64encode((_NOW_TIME + ',' + _UUID + ',' + _MD5 + ',' + _PostKeyVersion).encode()).decode()

    def login(self):
        """用户登录"""

        token_headers = {
            "pa": self.get_pa(),
            "appInfo": json.dumps(self.config['Headers']['appInfo']),
            "Connection": "close"
        }

        data = {
            "mobile": self.config['userInfo']['username'],
            "pwd": self.config['userInfo']['password']
        }

        res_json = self.rpost(
            _url=yarl.URL.build(
                scheme='https',
                host='pocketapi.48.cn',
                path='/user/api/v1/login/app/mobile'
            ),
            _headers=token_headers,
            _params=data
        )

        self.__login_user = LoginUserInfo(res_json['content']['userInfo'])
