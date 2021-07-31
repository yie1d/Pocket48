# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 ‏‎20:18
# @Author : XyD3°

import json, time


def WriteJson(new_dict, path):
    '''
    写json文件

    :param new_dict: 写入的字典
    :param path: 文件的位置及文件名
    '''
    with open(path, "w", encoding='utf-8') as f:
        json.dump(new_dict, f, ensure_ascii=False)
    f.close()


def ReadJson(path):
    '''
    读json文件

    :param path: 读取的文件位置
    :return: 字典
    '''
    with open(path, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    load_f.close()
    return load_dict


def Convert_to_Timestamp(date):
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


def Convert_to_Date(timestamp):
    '''
    时间戳转日期

    :param timestamp: 时间戳
    :return: 日期
    '''
    timeArray = time.localtime(timestamp / 1000 + 1)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    return otherStyleTime
