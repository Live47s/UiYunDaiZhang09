# coding=UTF-8
# 读取yaml文件
#
import yaml
def loadyaml(filename):
    try:

        files = open(filename,'r',encoding="utf-8",errors='ignore')
        data = yaml.load(files, Loader=yaml.FullLoader)
        return data
    except:
        files = open(filename, 'r', encoding='gbk')
        data = yaml.load(files, Loader=yaml.FullLoader)
        return data





#
#
# a = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/account/InsertInDatabase.yaml')
# print(len(a))
# print(a)
# #
#
