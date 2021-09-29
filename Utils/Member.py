from Libs.CustomError import RoomNotFound, UnknownError


class Member():
    def __init__(self, infor: dict):
        '''

        :param infor: 获得的成员信息
        '''
        infor = infor['content']["starInfo"]
        self.starName = infor.get("starName")
        self.userId = infor.get('userId')
        if infor.get('starGroupName') != infor.get('starTeamName'):
            self.team = infor.get('starGroupName') + ' ' + infor.get('starTeamName').replace(' ', '')
        else:
            self.team = infor.get('starGroupName')

    def addRoomId(self, infor: dict):
        '''
        添加房间id

        :param infor: 获得的房间信息
        '''
        if infor['message'] == 'OK':
            self.roomId = infor['content']['roomInfo']['roomId']
        elif infor['message'] == '房间不存在':
            raise RoomNotFound
        else:
            raise UnknownError

    def PrintAll(self):
        '''
        输出所有私有属性
        '''
        print(self.__dict__)
