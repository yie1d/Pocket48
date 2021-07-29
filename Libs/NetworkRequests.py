# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 ‏‎19:17
# @Author : XyD3°

from Libs.GetPA import get_Pa
from Libs.AnyMethods import read_json
import requests,time

class NetworkRequest():
    def __init__(self):
        """
        初始化

        """
        # 获取配置信息
        self.__config = read_json("../Config/Config.json")
        # 获取token
        self.__get_token()
        # 创建会话
        self.__session = requests.Session()
        self.__set_headers()

    def __get_token(self):
        """
        登录获取TOKEN值

        """
        # 设置headers，这三项不可缺少
        token_headers = {
            # 登录请求时PA不为空就行，随便设置
            "pa": "1",
            "appInfo": str(self.__config.get("HEADERS_Config").get("appInfo")),
            "Connection": "close"
        }
        # 请求参数
        data = {
            "mobile": self.__config.get("TOKEN_Config").get("mobile"),
            "pwd": self.__config.get("TOKEN_Config").get("pwd")
        }
        # 发起请求
        res = requests.post(
            'https://pocketapi.48.cn/user/api/v1/login/app/mobile',
            headers=token_headers,
            json=data, timeout=10)
        # 解析返回数据
        self.__token = res.json()['content']['token']

    def __set_headers(self):
        """
        设置请求头

        """
        self.__session.headers.update({
            # 每次更新headers重新获取PA值
            "pa": get_Pa(self.__config.get("PA_Config")),
            "appInfo": str(self.__config.get("HEADERS_Config").get("appInfo")),
            "User-Agent": self.__config.get("HEADERS_Config").get("User-Agent"),
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "pocketapi.48.cn",
            "Connection": "close",
            "Accept-Encoding": "gzip",
            "token": self.__token
        })

    def __requests_post(self, url:str, data=None):
        """
        post方法

        :param url: 访问网址
        :param data: 请求参数
        :return: 响应
        """
        # 防止因为网络原因出错，设置重复次数
        retryCount = 0
        while retryCount < 5:
            try:
                # 发起请求
                res = requests.post(url=url,json=data,headers=self.__session.headers,timeout=10)
                # PA 过期
                if res.json()['message'] == '请升级到最新版本':
                    self.__set_headers()
                # TOKEN过期
                elif res.json()['message'] in ['token解密失败', '非法授权']:
                    self.__get_token()
                    self.__set_headers()
                else:
                    return res.json()
            # 请求错误
            except requests.exceptions.RequestException:
                retryCount += 1
                # 等待3s
                time.sleep(3)

        return None


    def get_member_BasicInfor(self, **kwargs):
        """
        通过成员名(模糊搜索)/id(精确搜索)获取成员基本信息

        :param kwargs: name 成员名  member_id 成员id
        :return: post响应
        """
        # 传参name则模糊搜索
        if kwargs.get("name",False):
            data = {"content": kwargs.get("name"), "limit": 30}
            url = 'https://pocketapi.48.cn/search/api/search/v1/query'
        # 传参member_id则精确搜索
        elif kwargs.get("member_id",False):
            data = {"lastTime": 0, "memberId": kwargs.get("member_id"), "limit": 20}
            url = 'https://pocketapi.48.cn/user/api/v1/user/star/archives'
        # 错误传参
        else:
            return None

        return self.__requests_post(url, data)

    def get_gift_Infor(self,member_id,businessCode=2):
        """
        businessCode

        :param member_id: 成员id
        :param businessCode: 可以在0-3设置
        :return: post响应
        """
        data = {"businessCode": businessCode,"memberId": member_id}
        url = 'https://pocketapi.48.cn/gift/api/v1/gift/list'

        return self.__requests_post(url, data)

    def get_room_BasicInfor(self, member_id,type = 0):
        """
        获取口袋房间基本信息

        :param member_id: 成员id
        :param type: 好像只能设置0，设置其它的都是房间不存在
        :return: post响应
        """
        data = {"sourceId": member_id, "type": type}
        url = 'https://pocketapi.48.cn/im/api/v1/im/room/info/type/source'

        return self.__requests_post(url, data)

    def get_room_MemberChat(self,member_id, room_id,  nextTime=0,needTop1Msg=True):
        """
        获取成员房间聊天信息(进入房间能看到的信息)

        :param member_id: 成员id
        :param room_id: 房间id
        :param nextTime: 0为当前，其余的可以根据每次调用后返回的nextTime设置
        :param needTop1Msg: True和False测试的时候没发现区别
        :return: post响应
        """
        data = {"needTop1Msg": needTop1Msg, "nextTime": nextTime, "ownerId": member_id, "roomId": room_id}
        url = 'https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/homeowner'

        return self.__requests_post(url, data)

    def get_room_FansChat(self, member_id,room_id,  nextTime=0,needTop1Msg=True):
        """
        获取聚聚房间聊天信息(进入房间后左滑看到的信息)

        :param member_id: 成员id
        :param room_id: 房间id
        :param nextTime: 0为当前，其余的可以根据每次调用后返回的nextTime设置
        :param needTop1Msg: True和False测试的时候没发现区别
        :return: post响应
        """
        data = {"needTop1Msg": needTop1Msg, "nextTime": nextTime, "ownerId": member_id, "roomId": room_id}
        url = 'https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/all'

        return self.__requests_post(url, data)

    def get_room_OtherInfor(self,member_id, room_id,  type:str, nextTime=0):
        """
        其它信息(口袋房间上面的可选项)

        :param member_id: 成员id
        :param room_id: 房间id
        :param type: "USER_LIVE"直播、"OPEN_LIVE"公演、"WEI_BO"微博、"DOU_YIN"抖音等
        :param nextTime: 0为当前，其余的可以根据每次调用后返回的nextTime设置
        :return: post响应
        """
        data = {"nextTime": nextTime, "ownerId": member_id, "extMsgType": type, "roomId": room_id}
        url = 'https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/aim/type'

        return self.__requests_post(url, data)

    def get_room_Live(self, liveid):
        '''
        获取直播信息

        :param liveid: 直播id
        :return:
        '''
        data = {"liveId": liveid}
        url = 'https://pocketapi.48.cn/live/api/v1/live/getLiveOne'

        return self.__requests_post(url, data)

    @staticmethod
    def get_live_Barrage(url):
        """
        获取直播的弹幕

        :param url: 弹幕下载路径
        :return: 解析后的数据
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        res = requests.get(url,headers=headers)

        return res.content.decode()

    @staticmethod
    def get_jzb_Rank(name:str):
        '''
        获取饺子榜数据

        :param name: 成员姓名
        :return: 获取到的数据
        '''
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        url = 'https://www.jzb48.com/zx/api/get.php?type=detail&name=' + name
        res = requests.get(
            url=url,
            headers=headers
        )
        return res.content.decode('unicode_escape')

    @staticmethod
    def get_snh_memberid():
        '''
        官网名单

        :return: 获取到的数据
        '''
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        url = 'https://h5.48.cn/resource/jsonp/allmembers.php?gid'
        res = requests.get(
            url=url,
            headers=headers
        )
        return res.json()

    def get_im_infor(self):
        '''


        :return:
        '''
        url = 'https://pocketapi.48.cn/im/api/v1/im/userinfo'

        return self.__requests_post(url)

if __name__ == '__main__':
    m = NetworkRequest()
    # 农燕萍为例   memberid:417321  roomid:67313737
    # print(m.get_member_BasicInfor(name = "农燕萍")['content']['memberIndexTemplates'])
    # print(m.get_member_BasicInfor(member_id = 417321)['content'])
    # print(m.get_room_BasicInfor(417321))
    # print(m.get_gift_Infor(417321))
    # print(m.get_room_MemberChat(417321,67313737,0,False)['content'])
    # print(m.get_room_FansChat(417321,67313737,0,False)['content'])
    # print(m.get_room_OtherInfor(417321,67313737,"USER_LIVE",0)['content'])
    # print(m.get_room_Live(627290345307967488)['content'])



    # print(m.get_jzb_Rank('农燕萍'))
    # print(m.get_snh_memberid())
    # write_json(m.get_snh_memberid(),'../Config/allmembers_snh.json')

    # print(m.get_im_infor())




