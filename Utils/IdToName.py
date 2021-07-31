# -*- codeing = utf-8 -*-
# @Time : 2021/7/31 22:27
# @Author : XyD3°

from Libs.AnyMethods import ReadJson,WriteJson
from Libs.NetworkRequests import NetworkRequest

if __name__ == '__main__':
    NameDict = {}
    sess = NetworkRequest()

    ids = ReadJson('../Config/member.json')['toUserId']

    for id in ids :
        name = sess.GetMemberBasicInfo(userId=id)['content']["starInfo"]["starName"]
        print("\r"+name,end="\t\t\t\t\t")
        NameDict[name] = id

    WriteJson(NameDict,'../Config/IdToName.json')