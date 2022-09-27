from typing import Optional, List, Dict, Union


class BaseClass:
    def __init__(self, _raw_data: dict):
        """
        源数据管理
        """
        if not isinstance(_raw_data, dict):
            raise TypeError(f'接收数据类型错误，应该为字典类型，当前类型为：{type(_raw_data)}，传入数据：{_raw_data}')
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
            raise TypeError(f'接收数据类型错误，应该为字典类型，当前类型为：{type(_raw_data)}，传入数据：{_raw_data}')
        self.__raw_data = _raw_data


class UserInfo(BaseClass):
    def __init__(self, _raw_data: dict):
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            self.__dict__[f'__{k}'] = v

    @property
    def userId(self) -> Optional[int]:
        """用户id"""
        return self.__dict__.get('__userId')

    @property
    def nickname(self) -> Optional[str]:
        """用户名称"""
        return self.__dict__.get('__nickname')

    @property
    def avatar(self) -> Optional[str]:
        """头像url"""
        return self.__dict__.get('__avatar')


class Permission(BaseClass):
    def __init__(self, _raw_data: dict):
        """
        用户权限相关
        """
        super().__init__(_raw_data)

        self.raw_data = self.raw_data.get('post')

        for k, v in self.raw_data.items():
            self.__dict__[f'__{k}'] = v

    @property
    def view(self) -> Optional[bool]:
        return self.__dict__.get('__view')

    @property
    def create(self) -> Optional[bool]:
        return self.__dict__.get('__create')

    @property
    def update(self) -> Optional[bool]:
        return self.__dict__.get('__update')

    @property
    def delete(self) -> Optional[bool]:
        return self.__dict__.get('__delete')

    @property
    def managerGroup(self):
        return self.__dict__.get('__managerGroup')

    @property
    def managerTeam(self):
        return self.__dict__.get('__managerTeam')


class BindInfo(BaseClass):
    def __init__(self, _raw_data: dict):
        """
        绑定信息
        """
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            self.__dict__[f'__{k}'] = v

    @property
    def bindType(self) -> Optional[str]:
        """绑定平台"""
        return self.__dict__.get('__bindType')

    @property
    def uniqueId(self) -> Optional[str]:
        """uniqueId"""
        return self.__dict__.get('__uniqueId')

    @property
    def nickname(self) -> Optional[str]:
        """绑定平台用户名"""
        return self.__dict__.get('__nickname')


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
            self.__dict__[f'__{k}'] = v

    @property
    def relationship(self) -> Optional[bool]:
        """关系？"""
        return self.__dict__.get('__relationship')

    @property
    def bigUserInfo(self) -> UserInfo:
        return self.__dict__.get('__bigUserInfo')

    @property
    def smallUserInfo(self) -> UserInfo:
        return self.__dict__.get('__smallUserInfo')


class LoginUserInfo(UserInfo):
    def __init__(self, _raw_data: dict):
        super().__init__(_raw_data)

        for k, v in self.raw_data.items():
            if k == 'permission':
                v = Permission(v)
                self.__dict__[f'__{k}'] = v
            if k == 'bindInfo':
                v = [BindInfo(_info) for _info in v]
                self.__dict__[f'__{k}'] = v
            if k == 'bigSmallInfo':
                v = BigSmallInfo(v)
                self.__dict__[f'__{k}'] = v

    @property
    def exp(self) -> Optional[int]:
        """经验值"""
        return self.__dict__.get('__exp')

    @property
    def level(self) -> Optional[int]:
        """用户等级"""
        return self.__dict__.get('__level')

    @property
    def gender(self) -> Optional[int]:
        """性别"""
        return self.__dict__.get('__gender')

    @property
    def birthday(self) -> Optional[str]:
        """生日"""
        return self.__dict__.get('__birthday')

    @property
    def city(self) -> Optional[str]:
        """城市"""
        return self.__dict__.get('__city')

    @property
    def verification(self) -> Optional[bool]:
        """验证/认证？"""
        return self.__dict__.get('__verification')

    @property
    def money(self) -> Optional[int]:
        """鸡腿数"""
        return self.__dict__.get('__money')

    @property
    def support(self) -> Optional[int]:
        """鸡翅数"""
        return self.__dict__.get('__support')

    @property
    def permission(self) -> Optional[Permission]:
        """权限？"""
        return self.__dict__.get('__permission')

    @property
    def roleName(self) -> Optional[str]:
        """？？？"""
        return self.__dict__.get('__roleName')

    @property
    def roleId(self) -> Optional[int]:
        """?"""
        return self.__dict__.get('__roleId')

    @property
    def deviceId(self) -> Optional[str]:
        """设备序列号"""
        return self.__dict__.get('__deviceId')

    @property
    def bindInfo(self) -> Optional[List[BindInfo]]:
        """绑定信息"""
        return self.__dict__.get('__bindInfo')

    @property
    def badgeCount(self) -> Optional[int]:
        """徽章数量"""
        return self.__dict__.get('__badgeCount')

    @property
    def friends(self) -> Optional[int]:
        """关注人数"""
        return self.__dict__.get('__friends')

    @property
    def followers(self) -> Optional[int]:
        """??"""
        return self.__dict__.get('__followers')

    @property
    def token(self) -> Optional[str]:
        """用户token"""
        return self.__dict__.get('__token')

    @property
    def bigSmallInfo(self) -> Optional[BigSmallInfo]:
        """???"""
        return self.__dict__.get('__bigSmallInfo')

    @property
    def commentStatus(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('__commentStatus')

    @property
    def bgImg(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('__bgImg')

    @property
    def badge(self) -> List[str]:
        """徽章列表？"""
        return self.__dict__.get('__badge')

    @property
    def vip(self) -> Optional[bool]:
        """是否是vip"""
        return self.__dict__.get('__vip')

    @property
    def teamLogo(self) -> Optional:
        """队伍logo"""
        return self.__dict__.get('__teamLogo')

    @property
    def card(self) -> Optional[int]:
        """???"""
        return self.__dict__.get('__card')

    @property
    def expArr(self) -> Optional[List[int]]:
        """经验列表"""
        return self.__dict__.get('__expArr')

    @property
    def pfUrl(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('__pfUrl')

    @property
    def editImg(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('__editImg')

    @property
    def editName(self) -> Optional[str]:
        """???"""
        return self.__dict__.get('__editName')

    @property
    def teenagersPassword(self) -> Union[str, int]:
        """青少年模式密码"""
        return self.__dict__.get('__teenagersPassword')

    @property
    def adult(self) -> Optional[bool]:
        """是否成年"""
        return self.__dict__.get('__adult')

    @property
    def continueAuth(self) -> Optional[bool]:
        """是否需要二次验证"""
        return self.__dict__.get('__bool')

    @property
    def outOfCn(self) -> Optional[bool]:
        """???"""
        return self.__dict__.get('__outOfCn')

    @property
    def validTime(self) -> Optional[int]:
        """登录有效时间"""
        return self.__dict__.get('__validTime')

    @property
    def teenagersTips(self) -> Optional[str]:
        """青少年使用公告"""
        return self.__dict__.get('__teenagersTips')
