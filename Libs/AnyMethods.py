# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 ‏‎20:18
# @Author : XyD3°

import json, time, xlrd, xlwt
from xlutils3.copy import copy


def WriteJson(new_dict, path):
    '''
    写json文件

    :param new_dict: 写入的字典
    :param path: 文件的位置及文件名
    '''
    with open(path, "w") as f:
        json.dump(new_dict, f)
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


class WriteXls():
    def __init__(self, date,title:list):
        self.path = '../result/' + date + '口袋报.xls'
        # 创建文件
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet("总表")
        for i in range(len(title)):
            worksheet.write(0, i, title[i])
        workbook.save(self.path)

    def __openxls(self,sheetName = "XyD3"):
        # 打开工作簿
        workbook = xlrd.open_workbook(self.path)
        # 将xlrd对象拷贝转化为xlwt对象
        new_workbook = copy(workbook)
        if sheetName != "XyD3":
            worksheet_old = workbook.sheet_by_name(sheetName)
            # 获取表格中已存在的数据的行数
            rows_old = worksheet_old.nrows
            return new_workbook,rows_old

        return new_workbook

    def writexls(self,flag:bool,sheetName,data:list):
        if flag:
            # 新建表
            workbook = self.__openxls()
            worksheet = workbook.add_sheet(sheetName)
            for i in range(len(data)):
                worksheet.write(0, i, data[i])
        else:
            # 追加写一行数据
            workbook,rows = self.__openxls(sheetName)
            worksheet = workbook.get_sheet(0)
            for i in range(len(data)):
                worksheet.write(rows, i, data[i])
        workbook.save(self.path)


    def totalWrite(self,totalData):
        pass

    def oneMonthWrite(self,oneMonthData:dict):
        pass
        # for key in oneMonthData.keys():

if __name__ == '__main__':
    m = WriteXls("2",["1","2"])
    k = input("1")
    m.writexls(True,"np",["2","3",4])
    s = input("2")
    m.writexls(False,"总表",["s",3,5])
