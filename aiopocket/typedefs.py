from typing import Optional, List


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


class UserInfo(BaseClass):
    def __init__(self, _raw_data: dict):
        super().__init__(_raw_data)

        for k, v in _raw_data.items():
            self.__dict__[f'__{k}'] = v

        self.__nickname: Optional[str] = self.raw_data.get('nickname')
        self.__avatar: Optional[str] = self.raw_data.get('avatar')
        self.__exp: Optional[int] = self.raw_data.get('exp')
        self.__level: Optional[int] = self.raw_data.get('level')
        self.__gender: Optional[int] = self.raw_data.get('gender')
        self.__birthday: Optional[str] = self.raw_data.get('birthday')
        self.__city: Optional[str] = self.raw_data.get('city')
        self.__verification: Optional[bool] = self.raw_data.get('verification')
        self.__money: Optional[int] = self.raw_data.get('money')
        self.__support: Optional[int] = self.raw_data.get('support')
        self.__permission: Permission = Permission(self.raw_data.get('permission'))
        self.__roleName: Optional[str] = self.raw_data.get('roleName')
        self.__roleId: Optional[int] = self.raw_data.get('roleId')
        self.__deviceId: Optional[str] = self.raw_data.get('deviceId')
        self.__bindInfo: Optional[List[dict]] = self.raw_data.get('bindInfo')
        self.__badgeCount: Optional[int] = self.raw_data.get('badgeCount')
        self.__friends: Optional[int] = self.raw_data.get('friends')
        self.__followers: Optional[int] = self.raw_data.get('followers')
        self.__token: Optional[str] = self.raw_data.get('token')
        self.__bigSmallInfo = self.raw_data.get('bigSmallInfo')
        self.__commentStatus: Optional[int] = self.raw_data.get('commentStatus')

        self.__adult: Optional[bool] = True if self.raw_data.get('adult') == 'True' else False
        self.__badge: Optional[List[str]] = self.raw_data.get('badge')

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
        return Permission(self.__dict__.get('__permission'))

    # todo add others
    @property
    def adult(self) -> bool:
        """是否成年"""
        return self.__adult

    @property
    def badge(self) -> List[str]:
        """徽章列表？"""
        return self.__badge
