# coding=UTF-8
import os
from page_objeck.Basic.basicsetting.basicsetting_department_page import *

from config.yamlload import loadyaml
import allure


@pytest.mark.usefixtures('setting')
class TestCasedepartment():

    #  基础设置-新增部门
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-部门模块")
    @allure.story("新增部门")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/department/add.yaml'))
    def test_2_add_department(self, udata, init_driver):
        '''基础设置-新增客户用例'''
        self.lp = Basic_Setting_department(init_driver).add_department(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-查询部门
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-部门模块")
    @allure.story("查询部门")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/department/query.yaml'))
    def test_3_seach_department(self, udata, init_driver):
        '''基础设置-新增部门用例'''
        self.lp = Basic_Setting_department(init_driver).seach_department(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-修改部门
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-部门模块")
    @allure.story("修改部门名称")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/department/change.yaml'))
    def test_4_change_department(self, udata, init_driver):
        '''基础设置-新增部门用例'''
        self.lp = Basic_Setting_department(init_driver).change_department(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-删除部门
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-部门模块")
    @allure.story("删除单个部门")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/department/delete.yaml'))
    def test_5_delete_department(self, udata, init_driver):
        '''基础设置-新增客户用例'''
        self.lp =Basic_Setting_department(init_driver).delete_department(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


if __name__ == '__main__':
    # 获取当前年月日时分秒作为测试报告文件夹的后缀
    currentTime = time.strftime('%Y-%m-%d-%H-%M-%S')
    # 存储allure记录的运行日志
    # os.system(r'copy environment.properties D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/Allure-results')




    pytest.main(
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_basesetting/test_case_basic_department.py',
         '--alluredir', './Allure-results','--clean-alluredir',
         '-W','ignore:Module already imported:pytest.PytestWarning'])
    #
    # pytest.main(['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic_customer.py','--alluredir',
    #              './Allure-results','--clean-alluredir'])

    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')

    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ./Allure-report{currentTime}')