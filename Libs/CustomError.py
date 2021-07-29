# -*- codeing = utf-8 -*-
# @Time : 2021/7/29 14:03
# @Author : 

class RoomNotFound(Exception):
    '''
    房间不存在
    '''
    def __str__(self):
        '''
        错误信息

        :return:
        '''
        return '房间不存在'

class UnknownError(Exception):
    '''
    未知错误类型
    '''
    def __str__(self):
        '''

        :return:
        '''
        return '未知错误'