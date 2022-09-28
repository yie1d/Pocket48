import asyncio
import os
import json

from uuid import uuid1
from time import time
from hashlib import md5
from base64 import b64encode
from typing import List, Dict, Tuple, Optional, Union

import aiohttp
import toml
import yarl
import requests
from tenacity import retry as aretry, stop_after_attempt, wait_fixed
from retrying import retry

from .typedefs import LoginUserInfo, UserInfo, StarBasicInfo
from .exceptions import PocketTypeError


class Client:
    def __init__(self) -> None:
        """
        pocket48客户端
        """
        self.__config: Optional[dict] = None

        self.__uuid: Optional[str] = str(uuid1()).replace('-', '')
        self.__base_url = yarl.URL.build(scheme='https', host='pocketapi.48.cn')
        self.__login_user: Optional[LoginUserInfo] = LoginUserInfo({})
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
        if self.connector is not None:
            await self.connector.close()

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
                base_url=self.__base_url,
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
    def pa(self) -> str:
        """
        获取pa值
        """
        _PostKey = self.config['paInfo']['PostKey']
        _PostKeyVersion = self.config['paInfo']['PostKeyVersion']
        _UUID = self.__uuid
        _NOW_TIME = str(int(time() * 1000))
        _MD5 = md5((_NOW_TIME + _UUID + _PostKey).encode()).hexdigest()

        return b64encode((_NOW_TIME + ',' + _UUID + ',' + _MD5 + ',' + _PostKeyVersion).encode()).decode()

    @property
    def headers(self):
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
            self.user_login()

        return base_headers.update({
            'pa': self.pa,
            'token': self.__login_user.token
        })

    @staticmethod
    @retry(stop_max_attempt_number=3, wait_fixed=3)
    def __rpost(_url: yarl.URL, _params: Dict[str, str], _headers: Optional[Dict[str, str]] = None,
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

    def user_login(self):
        """用户登录"""

        token_headers = {
            "pa": self.pa,
            "appInfo": json.dumps(self.config['Headers']['appInfo']),
            "Connection": "close"
        }

        params = {
            "mobile": self.config['userInfo']['username'],
            "pwd": self.config['userInfo']['password']
        }

        res_json = self.__rpost(
            _url=yarl.URL.build(
                scheme='https',
                host='pocketapi.48.cn',
                path='/user/api/v1/login/app/mobile'
            ),
            _headers=token_headers,
            _params=params
        )

        self.__login_user = LoginUserInfo(res_json['content']['userInfo'])

    @aretry(stop=stop_after_attempt(5), wait=wait_fixed(3))
    async def __apost(self, _url: yarl.URL, _params: dict, _headers: Optional[dict] = None) -> dict:
        if _headers is None:
            _headers = self.headers

        async with self.__sem:
            async with self.session.post(
                    url=_url,
                    json=_params,
                    headers=_headers
            ) as resp:
                res_json = await resp.json()
                print(res_json)

        if res_json.get('message') in ['token解密失败', '非法授权']:
            self.user_login()
        else:
            return res_json

    async def get_starBasicInfo(self, _id: int) -> StarBasicInfo:
        """
        通过成员id获取成员基本信息
        """
        if isinstance(_id, int):
            url = yarl.URL.build(
                path='/user/api/v1/user/star/archives'
            )
            params = {
                'lastTime': 0,
                'memberId': _id,
                'limit': 20
            }
        else:
            raise PocketTypeError("类型错误！")

        res_json = await self.__apost(url, params)

        return StarBasicInfo(res_json['content'])
