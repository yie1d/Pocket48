# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 ‏‎20:18
# @Author : XyD3°

import json,time

def write_json(new_dict,path):
    '''
    写如json文件

    :param new_dict: 写入的字典
    :param path: 文件的位置及文件名
    '''
    with open(path,"w") as f:
        json.dump(new_dict, f)
    f.close()

def read_json(path):
    '''
    读json文件

    :param path: 读取的文件位置
    :return: 字典
    '''
    with open(path, 'r',encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    load_f.close()
    return load_dict

def convert_to_timestamp(date):
    '''
    日期转时间戳

    :param date: 时间  格式为 2021-07-15
    :return: 时间戳
    '''
    date = date + ' 00:00:00'
    # 转为时间数组
    end_timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    end_timeStamp = int(time.mktime(end_timeArray)) * 1000

    return end_timeStamp

def convert_to_date(timestamp):
    '''
    时间戳转日期

    :param timestamp: 时间戳
    :return: 日期
    '''
    timeArray = time.localtime(timestamp / 1000)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray).split(' ')

    return otherStyleTime

