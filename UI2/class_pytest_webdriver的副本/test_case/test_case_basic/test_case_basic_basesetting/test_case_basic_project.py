# coding=UTF-8
import os
from page_objeck.Basic.basicsetting.bascisetting_project_page import *

from config.yamlload import loadyaml
import allure




@pytest.mark.usefixtures('setting')
class TestCaseproject():
    # #  登录实现
    # @allure.epic("登录模块")
    # @allure.feature("账号存在用户登录测试")
    # @pytest.mark.parametrize('udata',loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/login/data.yaml'))
    # def test_1_login(self,udata,init_driver):
    #     '''测试登录用例'''
    #     self.lp = LgoinPage(init_driver)
    #     ourl = self.lp.login(udata['company'],udata['username'],udata['pwd'])
    #     assert udata['expectedurl'] in ourl
    #     # pytest.assume(udata['expectedurl'] == ourl)
    #     # 动态allure标题
    #     allure.dynamic.title(f'{udata["legend"]}')
    #     allure.attach(str([f"{udata['expectedurl']} 等于 {ourl}"]),"断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
    #     time.sleep(3)

    #  基础设置-新增项目
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-项目模块")
    @allure.story("新增项目")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/project/add.yaml'))
    def test_2_add_project(self, udata, init_driver):
        '''基础设置-新增项目用例'''
        self.lp = Basic_Setting_project(init_driver).add_project(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-查询客户
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-项目模块")
    @allure.story("查询项目")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/project/query.yaml'))
    def test_3_seach_project(self, udata, init_driver):
        '''基础设置-新增项目用例'''
        self.lp = Basic_Setting_project(init_driver).seach_project(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-修改项目
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-项目模块")
    @allure.story("修改项目名称")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/project/change.yaml'))
    def test_4_change_project(self, udata, init_driver):
        '''基础设置-新增客户用例'''
        self.lp = Basic_Setting_project(init_driver).change_project(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-删除项目
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-项目模块")
    @allure.story("删除单个项目")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/project/delete.yaml'))
    def test_5_delete_project(self, udata, init_driver):
        '''基础设置-新增项目用例'''
        self.lp = Basic_Setting_project(init_driver).delete_project(udata['customerName'])
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
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_basesetting/test_case_basic_project.py',
         '--alluredir', './Allure-results','--clean-alluredir',
         '-W','ignore:Module already imported:pytest.PytestWarning'])
    #
    # pytest.main(['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic_customer.py','--alluredir',
    #              './Allure-results','--clean-alluredir'])

    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')

    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ./Allure-report{currentTime}')