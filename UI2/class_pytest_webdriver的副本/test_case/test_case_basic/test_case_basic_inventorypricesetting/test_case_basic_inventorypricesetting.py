# coding=UTF-8
import os
from page_objeck.Basic.inventoryPriceSetting.basicsetting_inventorypricesetting_page import Basic_Setting_inventorypricesetting
from page_objeck.Basic.inventoryPriceSetting.basicsetting_inventorypricesetting_page import *
# from delete.login_page import *
from config.yamlload import loadyaml
import allure


@pytest.mark.usefixtures('inventoryPrice')
class TestCaseinventorypricesetting():

    #  基础设置-查询存货价格
    @allure.epic("基础设置模块")
    @allure.feature("存货价格模块")
    @allure.story("查询存货价格")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/inventoryPriceSetting/query.yaml'))
    def test_1_seach_inventorypricesetting(self, udata, init_driver):
        '''基础设置-新增存货价格用例'''
        self.lp = Basic_Setting_inventorypricesetting(init_driver).seach_inventorypricesetting(udata['customerName'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-修改存货价格
    @allure.epic("基础设置模块")
    @allure.feature("存货价格模块")
    @allure.story("修改存货价格名称")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/inventoryPriceSetting/change.yaml'))
    def test_4_change_customer(self, udata, init_driver):
        '''基础设置-新增存货价格用例'''
        self.lp = Basic_Setting_inventorypricesetting(init_driver).change_inventorypricesetting(udata['customerName'])
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
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_inventorypricesetting/test_case_basic_inventorypricesetting.py',
         '--alluredir', './Allure-results','--clean-alluredir',
         '-W','ignore:Module already imported:pytest.PytestWarning'])
    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')
    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ../Allure-report{currentTime}')