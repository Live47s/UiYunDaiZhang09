# coding=UTF-8
import os

from page_objeck.Fundsmanagement.Advancepayment.fundsmanagement_advancepayment_page import *
# from delete.login_page import *
from config.yamlload import loadyaml
import allure


@pytest.mark.usefixtures('AdvancePayment')
class TestCaseadvancepayment():

    #  基础设置-新增预付款单
    @allure.epic("资金管理")
    @allure.feature("预付款单模块")
    @allure.story("新增预付款单")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/advance payment/add.yaml'))
    def test_2_add_advancepayment(self, udata, init_driver):
        '''基础设置-新增预付款单用例'''
        self.lp = Fund_Management_advancepayment(init_driver).add_advancepayment(udata['Name'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-修改预付款单
    @allure.epic("资金管理")
    @allure.feature("预付款单模块")
    @allure.story("修改预付款单名称")
    @pytest.mark.parametrize('udata', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/advance payment/change.yaml'))
    def test_4_change_customer(self, udata, init_driver):
        '''基础设置-新增预付款单用例'''
        self.lp = Fund_Management_advancepayment(init_driver).change_advancepayment(udata['Name'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


    #  基础设置-删除客户
    @allure.epic("资金管理")
    @allure.feature("预付款单模块")
    @allure.story("删除单个预付款单")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/advance payment/delete.yaml'))
    def test_5_delete_customer(self, udata, init_driver):
        '''基础设置-删除预付款单用例'''
        self.lp = Fund_Management_advancepayment(init_driver).delete_advancepayment(udata['Name'])
        pytest.assume(self.lp == udata['message'])
        # 动态allure标题
        allure.dynamic.title(f'{udata["legend"]}')
        allure.attach(str([f"{udata['message']} 等于 {self.lp}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
        time.sleep(3)


if __name__ == '__main__':

    # 获取当前年月日时分秒作为测试报告文件夹的后缀
    currentTime = time.strftime('%Y-%m-%d-%H-%M-%S')
    # 存储allure记录的运行日志
    os.system(r'copy environment.properties D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/Allure-results')

    pytest.main(
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_fundsmanagement/test_case_fundsmanagement_advancepayment/test_case_fundsmanagement_advancepayment.py',
         '--alluredir', './Allure-results','--clean-alluredir',
         '-W','ignore:Module already imported:pytest.PytestWarning'])
    #
    # pytest.main(['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic_customer.py','--alluredir',
    #              './Allure-results','--clean-alluredir'])

    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')
    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ../Allure-report{currentTime}')




    # pytest.main(['-s', "test_get_port.py", "--alluredir=./report/allure_result"])
    #
    # # 将report目录下生成的json数据转换成html测试报告文件
    # os.system("allure generate ./report/allure_result -o ./report/html_result/ --clean")
    # # 打开报告。本机地址+自定义端口。
    # os.system("allure open -h 127.0.0.1 -p 8083 ./report/html_result")
