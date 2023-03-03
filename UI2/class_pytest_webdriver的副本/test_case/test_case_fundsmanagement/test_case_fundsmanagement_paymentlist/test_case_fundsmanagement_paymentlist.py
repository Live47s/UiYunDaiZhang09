# coding=UTF-8
import os

from page_objeck.Fundsmanagement.paymentList.fundsmanagement_paymentlist_page import *
# from delete.login_page import *
from config.yamlload import loadyaml
import allure


@pytest.mark.usefixtures('PaymentList')
class TestCasepaymentlist():

    #  基础设置-查询单据列表
    @allure.epic("资金管理")
    @allure.feature("单据列表模块")
    @allure.story("查询单据列表")
    @pytest.mark.parametrize('udata', loadyaml(
        'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/paymentlist/query.yaml'))
    def test_2_seach_paymentlist(self, udata, init_driver):
        '''基础设置-查询单据列表用例'''
        self.lp = Fund_Management_paymentlist(init_driver).seach_paymentlist(udata['customerName'])

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
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_fundsmanagement/test_case_fundsmanagement_paymentlist/test_case_fundsmanagement_paymentlist.py',
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
