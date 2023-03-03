# # coding=UTF-8
# import time,os
# import pytest
# from basicsetting_warhouse_page import *
# from base import login
# from page_objeck.login_page import *
# from config.yamlload import loadyaml
# import allure
# # TODO
#
# @pytest.mark.usefixtures('setting')
# class TestCaseWarhouse():
#
#     #  基础设置-新增仓库
#     @allure.epic("基础设置模块")
#     @allure.feature("基础资料-仓库模块")
#     @allure.story("新增仓库")
#     @pytest.mark.parametrize('udata', loadyaml(
#         'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/warhouse/add.yaml'))
#     def test_2_add_warhouse(self, udata, init_driver):
#         '''基础设置-新增客户用例'''
#         self.lp = Basic_Setting_Warhouse(init_driver).add_Warhouse(udata['customerName'],udata['phone'])
#         pytest.assume(self.lp == udata['message'])
#         # 动态allure标题
#         allure.dynamic.title(f'{udata["legend"]}')
#         allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
#         time.sleep(3)
#
#
#     #  基础设置-查询仓库
#     @allure.epic("基础设置模块")
#     @allure.feature("基础资料-仓库模块")
#     @allure.story("查询仓库")
#     @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/warhouse/query.yaml'))
#     def test_3_seach_warhouse(self, udata, init_driver):
#         '''基础设置-新增仓库用例'''
#         self.lp = Basic_Setting_Warhouse(init_driver).seach_Warhouse(udata['customerName'])
#         pytest.assume(self.lp == udata['message'])
#         # 动态allure标题
#         allure.dynamic.title(f'{udata["legend"]}')
#         allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
#         time.sleep(3)
#
#
#     #  基础设置-修改仓库
#     @allure.epic("基础设置模块")
#     @allure.feature("基础资料-仓库模块")
#     @allure.story("修改仓库名称")
#     @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/warhouse/change.yaml'))
#     def test_4_change_warhouse(self, udata, init_driver):
#         '''基础设置-新增仓库用例'''
#         self.lp = Basic_Setting_Warhouse(init_driver).change_Warhouse(udata['customerName'])
#         pytest.assume(self.lp == udata['message'])
#         # 动态allure标题
#         allure.dynamic.title(f'{udata["legend"]}')
#         allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
#         time.sleep(3)
#
#
#     #  基础设置-删除仓库
#     @allure.epic("基础设置模块")
#     @allure.feature("基础资料-仓库模块")
#     @allure.story("删除单个仓库")
#     @pytest.mark.parametrize('udata', loadyaml(
#         'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/warhouse/delete.yaml'))
#     def test_5_delete_warhouse(self, udata, init_driver):
#         '''基础设置-新增客户用例'''
#         self.lp =Basic_Setting_Warhouse(init_driver).delete_Warhouse(udata['customerName'])
#         pytest.assume(self.lp == udata['message'])
#         # 动态allure标题
#         allure.dynamic.title(f'{udata["legend"]}')
#         allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
#         time.sleep(3)
#
#
# if __name__ == '__main__':
#     # 获取当前年月日时分秒作为测试报告文件夹的后缀
#     currentTime = time.strftime('%Y-%m-%d-%H-%M-%S')
#     # 存储allure记录的运行日志
#     # os.system(r'copy environment.properties D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/Allure-results')
#
#
#
#
#     pytest.main(
#         ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_warhouse.py',
#          '--alluredir', './Allure-results','--clean-alluredir',
#          '-W','ignore:Module already imported:pytest.PytestWarning'])
#     #
#     # pytest.main(['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic_customer.py','--alluredir',
#     #              './Allure-results','--clean-alluredir'])
#
#     # 生成测试报告，找到测试数据 生成测试报告
#     os.system('allure serve ./Allure-results -o ./reports')
#
#     # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
#     os.system(f'allure generate ./Allure-results -o ./Allure-report{currentTime}')