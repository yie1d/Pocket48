from typing import Optional, List, Dict, Union
from .exceptions import PocketTypeError


class BaseClass:
    def __init__(self, _raw_data: dict):
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
    def raw_data(self, _raw_data: dict):
        if not isinstance(_raw_data, dict):
            raise PocketTypeError(f'接收数据类型错误，应该为字典类型，当前类型为：{type(_raw_data)}，传入数据：{_raw_data}')
        self.__raw_data = _raw_data


class UserInfo(BaseClass):
    def __init__(self, _raw_data: dict):
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


class Permission(BaseClass):
    def __init__(self, _raw_data: dict):
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
    def __init__(self, _raw_data: dict):
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
    def __init__(self, _raw_data: dict):
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
    def __init__(self, _raw_data: dict):
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
    def level(self) -> Optional[int]:
        """用户等级"""
        return self.__dict__.get('level')

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
    def friends(self) -> Optional[int]:
        """关注人数"""
        return self.__dict__.get('friends')

    @property
    def followers(self) -> Optional[int]:
        """??"""
        return self.__dict__.get('followers')

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
    def bgImg(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('bgImg')

    @property
    def badge(self) -> List[str]:
        """徽章列表？"""
        return self.__dict__.get('badge')

    @property
    def vip(self) -> Optional[bool]:
        """是否是vip"""
        return self.__dict__.get('vip')

    @property
    def teamLogo(self) -> Optional:
        """队伍logo"""
        return self.__dict__.get('teamLogo')

    @property
    def card(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('card')

    @property
    def expArr(self) -> Optional[List[int]]:
        """经验列表"""
        return self.__dict__.get('expArr')

    @property
    def pfUrl(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('pfUrl')

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
    def __init__(self, _raw_data: dict):
        """
        xox基础信息
        """
        super().__init__(_raw_data)

    @property
    def starName(self) -> Optional[str]:
        """xox姓名"""
        return self.__dict__.get('starName')

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
    def __init__(self, _raw_data: dict):
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
    """查询到的信息"""
    def __init__(self, _raw_data):
        self.starInfo = StarUserInfo(_raw_data['starInfo'])
        self.fansRank = [UserInfo(fans) for fans in _raw_data['fansRank']]
        self.history = [StarHistory(_history) for _history in _raw_data['history']]
