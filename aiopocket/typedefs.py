from typing import Optional, List, Dict, Union
from .exceptions import PocketTypeError


class BaseClass:
    def __init__(self, _raw_data: dict) -> None:
        """
        源数据管理
        """
        if not isinstance(_raw_data, dict):
            raise PocketTypeError(f'接收数据类型错误，应该为字典类型，当前类型为：{type(_raw_data)}，传入数据：{_raw_data}')
        self.__raw_data = _raw_data

    @property
    def raw_data(self) -> dict:
        """
        源数据
        """
        return self.__raw_data

    @raw_data.setter
    def raw_data(self, _raw_data: dict) -> None:
        if not isinstance(_raw_data, dict):
            raise PocketTypeError(f'接收数据类型错误，应该为字典类型，当前类型为：{type(_raw_data)}，传入数据：{_raw_data}')
        self.__raw_data = _raw_data


class UserInfo(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            self.__dict__[k] = v

    @property
    def userId(self) -> Optional[int]:
        """用户id"""
        return self.__dict__.get('userId')

    @property
    def nickname(self) -> Optional[str]:
        """用户昵称"""
        return self.__dict__.get('nickname')

    @property
    def avatar(self) -> Optional[str]:
        """头像url"""
        return self.__dict__.get('avatar')

    @property
    def badge(self) -> Optional[List[str]]:
        """徽章列表？"""
        return self.__dict__.get('badge')

    @property
    def level(self) -> Optional[int]:
        """用户等级"""
        return self.__dict__.get('level')

    @property
    def isStar(self) -> Optional[bool]:
        """是否是xox"""
        return self.__dict__.get('isStar')

    @property
    def friends(self) -> Optional[int]:
        """关注人数"""
        return self.__dict__.get('friends')

    @property
    def followers(self) -> Optional[int]:
        """收到鲜花？"""
        return self.__dict__.get('followers')

    @property
    def teamLogo(self) -> Optional[str]:
        """队伍logo"""
        return self.__dict__.get('teamLogo')

    @property
    def signature(self) -> Optional[str]:
        """签名？"""
        return self.__dict__.get('signature')

    @property
    def bgImg(self) -> Optional[str]:
        """背景图片？"""
        return self.__dict__.get('bgImg')

    @property
    def vip(self) -> Optional[bool]:
        """是否是vip"""
        return self.__dict__.get('vip')

    @property
    def userRole(self) -> Optional[int]:
        """用户角色  xox好像是3  普通用户是1"""
        return self.__dict__.get('userRole')

    @property
    def pfUrl(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('pfUrl')

    @property
    def effectUser(self) -> Optional[bool]:
        """是否是影响用户"""
        return self.__dict__.get('effectUser')

    @property
    def realNickName(self) -> Optional[str]:
        """用户自定义呢称"""
        return self.__dict__.get('realNickName')

    @property
    def starName(self) -> Optional[str]:
        """xox姓名"""
        return self.__dict__.get('starName')

    @property
    def star(self) -> Optional[bool]:
        """是否是xox"""
        return self.__dict__.get('star')


class Permission(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        """
        用户权限相关
        """
        super().__init__(_raw_data)

        self.raw_data = self.raw_data.get('post')

        for k, v in self.raw_data.items():
            self.__dict__[k] = v

    @property
    def view(self) -> Optional[bool]:
        return self.__dict__.get('view')

    @property
    def create(self) -> Optional[bool]:
        return self.__dict__.get('create')

    @property
    def update(self) -> Optional[bool]:
        return self.__dict__.get('update')

    @property
    def delete(self) -> Optional[bool]:
        return self.__dict__.get('delete')

    @property
    def managerGroup(self):
        return self.__dict__.get('managerGroup')

    @property
    def managerTeam(self):
        return self.__dict__.get('managerTeam')


class BindInfo(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        """
        绑定信息
        """
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            self.__dict__[k] = v

    @property
    def bindType(self) -> Optional[str]:
        """绑定平台"""
        return self.__dict__.get('bindType')

    @property
    def uniqueId(self) -> Optional[str]:
        """uniqueId"""
        return self.__dict__.get('uniqueId')

    @property
    def nickname(self) -> Optional[str]:
        """绑定平台用户名"""
        return self.__dict__.get('nickname')


class BigSmallInfo(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        """
        两个用户之间的关系类？
        """
        super().__init__(_raw_data)

        for k, v in _raw_data.items():
            if k == 'smallUserInfo':
                v = [UserInfo(_userInfo) for _userInfo in v]
            if k in 'bigUserInfo':
                v = UserInfo(v)
            self.__dict__[k] = v

    @property
    def relationship(self) -> Optional[bool]:
        """关系？"""
        return self.__dict__.get('relationship')

    @property
    def bigUserInfo(self) -> UserInfo:
        return self.__dict__.get('bigUserInfo')

    @property
    def smallUserInfo(self) -> UserInfo:
        return self.__dict__.get('smallUserInfo')


class LoginUserInfo(UserInfo):
    def __init__(self, _raw_data: dict) -> None:
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            if k == 'permission':
                v = Permission(v)
                self.__dict__[k] = v
            if k == 'bindInfo':
                v = [BindInfo(_info) for _info in v]
                self.__dict__[k] = v
            if k == 'bigSmallInfo':
                v = BigSmallInfo(v)
                self.__dict__[k] = v

    @property
    def exp(self) -> Optional[int]:
        """经验值"""
        return self.__dict__.get('exp')

    @property
    def gender(self) -> Optional[int]:
        """性别"""
        return self.__dict__.get('gender')

    @property
    def birthday(self) -> Optional[str]:
        """生日"""
        return self.__dict__.get('birthday')

    @property
    def city(self) -> Optional[str]:
        """城市"""
        return self.__dict__.get('city')

    @property
    def verification(self) -> Optional[bool]:
        """验证/认证？"""
        return self.__dict__.get('verification')

    @property
    def money(self) -> Optional[int]:
        """鸡腿数"""
        return self.__dict__.get('money')

    @property
    def support(self) -> Optional[int]:
        """鸡翅数"""
        return self.__dict__.get('support')

    @property
    def permission(self) -> Optional[Permission]:
        """权限？"""
        return self.__dict__.get('permission')

    @property
    def roleName(self) -> Optional[str]:
        """？？？"""
        return self.__dict__.get('roleName')

    @property
    def roleId(self) -> Optional[int]:
        """?"""
        return self.__dict__.get('roleId')

    @property
    def deviceId(self) -> Optional[str]:
        """设备序列号"""
        return self.__dict__.get('deviceId')

    @property
    def bindInfo(self) -> Optional[List[BindInfo]]:
        """绑定信息"""
        return self.__dict__.get('bindInfo')

    @property
    def badgeCount(self) -> Optional[int]:
        """徽章数量"""
        return self.__dict__.get('badgeCount')

    @property
    def token(self) -> Optional[str]:
        """用户token"""
        return self.__dict__.get('token')

    @property
    def bigSmallInfo(self) -> Optional[BigSmallInfo]:
        """???"""
        return self.__dict__.get('bigSmallInfo')

    @property
    def commentStatus(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('commentStatus')

    @property
    def card(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('card')

    @property
    def expArr(self) -> Optional[List[int]]:
        """经验列表"""
        return self.__dict__.get('expArr')

    @property
    def editImg(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('editImg')

    @property
    def editName(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('editName')

    @property
    def teenagersPassword(self) -> Union[str, int]:
        """青少年模式密码"""
        return self.__dict__.get('teenagersPassword')

    @property
    def adult(self) -> Optional[bool]:
        """是否成年"""
        return self.__dict__.get('adult')

    @property
    def continueAuth(self) -> Optional[bool]:
        """是否需要二次验证"""
        return self.__dict__.get('bool')

    @property
    def outOfCn(self) -> Optional[bool]:
        """???"""
        return self.__dict__.get('outOfCn')

    @property
    def validTime(self) -> Optional[int]:
        """登录有效时间"""
        return self.__dict__.get('validTime')

    @property
    def teenagersTips(self) -> Optional[str]:
        """青少年使用公告"""
        return self.__dict__.get('teenagersTips')


class StarUserInfo(UserInfo):
    def __init__(self, _raw_data: dict) -> None:
        """
        xox基础信息
        """
        super().__init__(_raw_data)

    @property
    def starAvatar(self) -> Optional[str]:
        """xox头像"""
        return self.__dict__.get('starAvatar')

    @property
    def starGroupId(self) -> Optional[int]:
        """xox分部id"""
        return self.__dict__.get('starGroupId')

    @property
    def starGroupName(self) -> Optional[str]:
        """xox分部名称"""
        return self.__dict__.get('starGroupName')

    @property
    def starTeamId(self) -> Optional[int]:
        """xox队伍id"""
        return self.__dict__.get('starTeamId')

    @property
    def starTeamName(self) -> Optional[str]:
        """xox队伍名称"""
        return self.__dict__.get('starTeamName')

    @property
    def periodId(self) -> Optional[int]:
        """xox期数id"""
        return self.__dict__.get('periodId')

    @property
    def periodName(self) -> Optional[str]:
        """xox期数名称"""
        return self.__dict__.get('periodName')

    @property
    def starTeamLogo(self) -> Optional[str]:
        """xox队伍logo"""
        return self.__dict__.get('starTeamLogo')

    @property
    def pinyin(self) -> Optional[str]:
        """xox姓名拼音"""
        return self.__dict__.get('pinyin')

    @property
    def abbr(self) -> Optional[str]:
        """xox姓名首字母？"""
        return self.__dict__.get('abbr')

    @property
    def joinTime(self) -> Optional[str]:
        """xox加入日期"""
        return self.__dict__.get('joinTime')

    @property
    def wbUid(self) -> Optional[str]:
        """xox微博uid"""
        return self.__dict__.get('wbUid')

    @property
    def wbName(self) -> Optional[str]:
        """xox微博名称"""
        return self.__dict__.get('wbName')

    @property
    def height(self) -> Optional[str]:
        """xox身高"""
        return self.__dict__.get('height')

    @property
    def bloodType(self) -> Optional[str]:
        """xox血型"""
        return self.__dict__.get('bloodType')

    @property
    def birthday(self) -> Optional[str]:
        """xox生日"""
        return self.__dict__.get('birthday')

    @property
    def constellation(self) -> Optional[str]:
        """xox星座"""
        return self.__dict__.get('constellation')

    @property
    def starRegion(self) -> Optional[str]:
        """xox星座区域？？？"""
        return self.__dict__.get('starRegion')

    @property
    def birthplace(self) -> Optional[str]:
        """xox出生地"""
        return self.__dict__.get('birthplace')

    @property
    def specialty(self) -> Optional[str]:
        """xox性格"""
        return self.__dict__.get('specialty')

    @property
    def hobbies(self) -> Optional[str]:
        """xox爱好"""
        return self.__dict__.get('hobbies')

    @property
    def fullPhoto1(self) -> Optional[str]:
        """xox全身照1"""
        return self.__dict__.get('fullPhoto1')

    @property
    def fullPhoto2(self) -> Optional[str]:
        """xox全身照2"""
        return self.__dict__.get('fullPhoto2')

    @property
    def fullPhoto3(self) -> Optional[str]:
        """xox全身照3"""
        return self.__dict__.get('fullPhoto3')

    @property
    def fullPhoto4(self) -> Optional[str]:
        """xox全身照4"""
        return self.__dict__.get('fullPhoto4')

    @property
    def status(self) -> Optional[int]:
        """xox状态？"""
        return self.__dict__.get('status')


class StarHistory(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        """经历类"""
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            self.__dict__[k] = v

    @property
    def ctime(self) -> Optional[str]:
        """发生时间"""
        return self.__dict__.get('ctime')

    @property
    def content(self) -> Optional[str]:
        """发生时间"""
        return self.__dict__.get('content')


class StarBasicInfo:
    def __init__(self, _raw_data: dict):
        """查询到的信息"""
        self.__dict__['starInfo'] = StarUserInfo(_raw_data['starInfo'])
        self.__dict__['fansRank'] = [UserInfo(fans) for fans in _raw_data['fansRank']]
        self.__dict__['history'] = [StarHistory(_history) for _history in _raw_data['history']]

    @property
    def starInfo(self) -> StarUserInfo:
        """xox信息"""
        return self.__dict__.get('starInfo')

    @property
    def fansRank(self) -> List[UserInfo]:
        """粉丝排名"""
        return self.__dict__.get('fansRank')

    @property
    def history(self) -> List[StarHistory]:
        """xox历史经历"""
        return self.__dict__.get('history')


class UserBasicInfo(BaseClass):
    def __init__(self, _raw_data: dict) -> None:
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            if k == 'baseUserInfo':
                v = UserInfo(v)
            self.__dict__[k] = v

    @property
    def baseUserInfo(self) -> UserInfo:
        """用户基础信息"""
        return self.__dict__.get('baseUserInfo')

    @property
    def isFriend(self) -> Optional[bool]:
        """是否是朋友"""
        return self.__dict__.get('isFriend')

    @property
    def relationship(self) -> Optional[int]:
        """关系"""
        return self.__dict__.get('relationship')

    @property
    def topRank(self) -> Optional[list]:
        """??"""
        return self.__dict__.get('topRank')

    @property
    def clubCount(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('clubCount')

    @property
    def rankNum(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('rankNum')

    @property
    def inBlacklist(self) -> Optional[bool]:
        """是否黑名单"""
        return self.__dict__.get('inBlacklist')

    @property
    def qingni(self) -> Optional:
        """？？？"""
        return self.__dict__.get('qingni')

    @property
    def friend(self) -> Optional[bool]:
        """朋友？"""
        return self.__dict__.get('friend')


class RoomInfo(BaseClass):
    def __init__(self, _raw_data: dict):
        super().__init__(_raw_data)

        for k, v in _raw_data.items():
            self.__dict__[k] = v

    @property
    def roomId(self) -> Optional[str]:
        """房间id"""
        return self.__dict__.get('roomId')

    @property
    def chatRoomId(self) -> Optional[str]:
        """聊天房间id"""
        return self.__dict__.get('chatRoomId')

    @property
    def roomName(self) -> Optional[str]:
        """房间名称"""
        return self.__dict__.get('roomName')

    @property
    def roomAvatar(self) -> Optional[str]:
        """房间头像"""
        return self.__dict__.get('roomAvatar')

    @property
    def roomTopic(self) -> Optional[str]:
        """房间话题"""
        return self.__dict__.get('roomTopic')

    @property
    def ctime(self) -> Optional[str]:
        """房间创建时间"""
        return self.__dict__.get('ctime')

    @property
    def roomType(self) -> Optional[int]:
        """房间类型"""
        return self.__dict__.get('roomType')

    @property
    def chatType(self) -> Optional[int]:
        """聊天类型"""
        return self.__dict__.get('chatType')

    @property
    def ownerId(self) -> Optional[str]:
        """房主id"""
        return self.__dict__.get('ownerId')

    @property
    def ownerName(self) -> Optional[str]:
        """房主名称"""
        return self.__dict__.get('ownerName')

    @property
    def icon(self) -> Optional[List[str]]:
        """房间icon"""
        return self.__dict__.get('icon')

    @property
    def bubbleId(self) -> Optional[str]:
        """气泡id"""
        return self.__dict__.get('bubbleId')

    @property
    def bgImg(self) -> Optional[str]:
        """背景图片"""
        return self.__dict__.get('bgImg')

    @property
    def welcomeMessage(self) -> Optional[str]:
        """房间欢迎信息"""
        return self.__dict__.get('welcomeMessage')

    @property
    def welcomeManagerName(self) -> Optional[str]:
        """欢迎管理员名称"""
        return self.__dict__.get('welcomeManagerName')

    @property
    def welcomeManagerId(self) -> Optional[str]:
        """欢迎管理员id"""
        return self.__dict__.get('welcomeManagerId')

    @property
    def welcomeManagerAvatar(self) -> Optional[str]:
        """欢迎管理员头像"""
        return self.__dict__.get('welcomeManagerAvatar')

    @property
    def replyKey(self) -> Optional[List]:
        """回复密钥"""
        return self.__dict__.get('replyKey')

    @property
    def qingNi(self) -> Optional[bool]:
        """？？？"""
        return self.__dict__.get('qingNi')

    @property
    def redPackageIcon(self) -> Optional[str]:
        """红包图标"""
        return self.__dict__.get('redPackageIcon')

    @property
    def managerAuditExplain(self) -> Optional[str]:
        """管理员申请信息"""
        return self.__dict__.get('managerAuditExplain')

    @property
    def crm(self) -> Optional[str]:
        """？？？"""
        return self.__dict__.get('crm')

    @property
    def chatStatus(self) -> Optional[int]:
        """聊天状态"""
        return self.__dict__.get('chatStatus')

    @property
    def ownerPf(self) -> Optional[str]:
        """房主pf"""
        return self.__dict__.get('ownerPf')


class UserFunction(BaseClass):
    def __init__(self, _raw_data: dict):
        """用户功能"""
        super().__init__(_raw_data)

        for k, v in _raw_data.items():
            self.__dict__[k] = v

    @property
    def sendText(self) -> Optional[bool]:
        """发送文本"""
        return self.__dict__.get('sendText')

    @property
    def sendImage(self) -> Optional[bool]:
        """发送图片"""
        return self.__dict__.get('sendImage')

    @property
    def sendVideo(self) -> Optional[bool]:
        """发送视频"""
        return self.__dict__.get('sendVideo')

    @property
    def sendVoice(self) -> Optional[bool]:
        """发送语音"""
        return self.__dict__.get('sendVoice')

    @property
    def sendGif(self) -> Optional[bool]:
        """发送gif"""
        return self.__dict__.get('sendGif')

    @property
    def sendEmoticon(self) -> Optional[bool]:
        """发送表情"""
        return self.__dict__.get('sendEmoticon')

    @property
    def sendForward(self) -> Optional[bool]:
        """转发"""
        return self.__dict__.get('sendForward')

    @property
    def sendGift(self) -> Optional[bool]:
        """发送礼物"""
        return self.__dict__.get('sendGift')

    @property
    def openAudio(self) -> Optional[bool]:
        """发送音频"""
        return self.__dict__.get('openAudio')

    @property
    def cdTime(self) -> Optional[int]:
        """发送间隔？"""
        return self.__dict__.get('cdTime')

    @property
    def normalRedPackage(self) -> Optional[bool]:
        """普通红包"""
        return self.__dict__.get('normalRedPackage')

    @property
    def passwordRedPackage(self) -> Optional[bool]:
        """密码红包"""
        return self.__dict__.get('passwordRedPackage')

    @property
    def specicalRedPackage(self) -> Optional[bool]:
        """特殊红包"""
        return self.__dict__.get('specicalRedPackage')

    @property
    def welcomeMessage(self) -> Optional[bool]:
        """欢迎消息"""
        return self.__dict__.get('welcomeMessage')

    @property
    def replyMessage(self) -> Optional[bool]:
        """回复消息"""
        return self.__dict__.get('replyMessage')

    @property
    def roomTitle(self) -> Optional[bool]:
        """设置房间标题"""
        return self.__dict__.get('roomTitle')

    @property
    def roomTopic(self) -> Optional[bool]:
        """设置房间话题"""
        return self.__dict__.get('roomTopic')


class UserConfig(BaseClass):
    def __init__(self, _raw_data: dict):
        super().__init__(_raw_data)

        for k, v in _raw_data.items():
            self.__dict__[k] = v

    @property
    def bgImg(self) -> Optional[str]:
        """背景图片"""
        return self.__dict__.get('bgImg')

    @property
    def bubbleId(self) -> Optional[str]:
        """气泡id"""
        return self.__dict__.get('bubbleId')


class BaseRoomInfo:
    def __init__(self, _raw_data: dict):
        for k, v in _raw_data.items():
            if k == 'roomInfo':
                v = RoomInfo(v)
            elif k == 'userFunction':
                v = UserFunction(v)
            elif k == 'userConfig':
                v = UserConfig(v)

            self.__dict__[k] = v

    @property
    def roomInfo(self) -> Optional[RoomInfo]:
        """房间信息"""
        return self.__dict__.get('roomInfo')

    @property
    def userFunction(self) -> Optional[UserFunction]:
        """用户权限"""
        return self.__dict__.get('userFunction')

    @property
    def roomRole(self) -> Optional[str]:
        """房间角色？"""
        return self.__dict__.get('roomRole')

    @property
    def userConfig(self) -> Optional[UserConfig]:
        """用户设置"""
        return self.__dict__.get('userConfig')

    @property
    def managerName(self) -> Optional[str]:
        """管理员名称"""
        return self.__dict__.get('managerName')

    @property
    def openAnonymousStatus(self) -> Optional[int]:
        """打开匿名状态？"""
        return self.__dict__.get('openAnonymousStatus')


