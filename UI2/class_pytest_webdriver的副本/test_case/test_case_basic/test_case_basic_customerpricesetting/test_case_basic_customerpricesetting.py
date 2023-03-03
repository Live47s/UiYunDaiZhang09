# coding=UTF-8
import os
from page_objeck.Basic.customerPriceSetting.bascisetting_customerpricesetting_page import *
# from delete.login_page import *
from config.yamlload import loadyaml
import allure


@pytest.mark.usefixtures('customerPrice')
class TestCasecustomerpricesetting():

    #  基础设置-新增客户价格设置
    @allure.epic("基础设置模块")
    @allure.feature("基础资料-客户价格设置模块")
    @allure.story("新增客户价格设置")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/customerpricesetting/add.yaml'))
    def test_1_add_customerpricesetting(self, udata, init_driver):
        '''基础设置-新增客户价格设置用例'''
        self.lp = Basic_Setting_customerpricesetting(init_driver).add_customerpricesetting(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-修改客户价格设置价格
    @allure.epic("基础设置模块")
    @allure.feature("客户价格设置价格模块")
    @allure.story("修改客户价格设置价格信息")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/customerpricesetting/change.yaml'))
    def test_2_change_customerpricesetting(self, udata, init_driver):
        '''基础设置-新增客户价格设置价格用例'''
        self.lp = Basic_Setting_customerpricesetting(init_driver).change_customerpricesetting(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)

    #  基础设置-删除客户价格设置
    @allure.epic("基础设置模块")
    @allure.feature("客户价格设置模块")
    @allure.story("删除客户价格设置")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/customerpricesetting/delete.yaml'))
    def test_3_deltle_customerpricesetting(self, udata, init_driver):
        '''基础设置-新增客户价格设置用例'''
        self.lp = Basic_Setting_customerpricesetting(init_driver).delete_customerpricesetting(udata['customerName'])
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
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_customerpricesetting/test_case_basic_customerpricesetting.py',
         '--alluredir', './Allure-results','--clean-alluredir',
         '-W','ignore:Module already imported:pytest.PytestWarning'])
    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')
    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ../Allure-report{currentTime}')