# coding=gbk
import os, time, pytest,allure

if __name__ == '__main__':

    # 获取当前年月日时分秒作为测试报告文件夹的后缀
    currentTime = time.strftime('%Y-%m-%d-%H-%M-%S')
    # 存储allure记录的运行日志
    os.system(r'copy environment.properties D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/Users/shs/class_pytest_webdriver/Allure-results')

    # # 运行test_case目录下所有以test开头的文件（所有用例）
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/', '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W','ignore:Module already imported:pytest.PytestWarning'])


    # 运行基础设置模块的所有用例
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic', '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])

    # 运行基础设置-基础资料模块的所有用例
    pytest.main(
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_basesetting', '--alluredir', './Allure-results','--clean-alluredir',
         '-W', 'ignore:Module already imported:pytest.PytestWarning'])

    # # 运行基础设置-存货价格设置模块的所有用例
    # pytest.main(
    #     ['-s',
    #      'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_inventorypricesetting',
    #      '--alluredir', './Allure-results', '--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])
    #

    # # #运行基础设置-客户模块的所有用例
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_customer.py',
    #      '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W','ignore:Module already imported:pytest.PytestWarning'])


    # # 运行基础设置-供应商模块的所有用例
    # pytest.main(
    #     ['-s',
    #      'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/test_case/test_case_basic/test_case_basic_supplier.py',
    #      '--alluredir', './Allure-results', '--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])



    # 生成测试报告，找到测试数据 生成测试报告
    os.system('allure serve ./Allure-results -o ./reports')
    # 生成测试报告，找到测试数据 生成测试报告，并在文件夹后缀上加上年月日时分秒
    os.system(f'allure generate ./Allure-results -o ./Allure-report{currentTime}')
    currentTime1 = time.strftime('%Y-%m-%d-%H-%M-%S')
    print('开始时间：'+currentTime)
    print('结束时间：' + currentTime1)
    # os.mkdir(path)  # 创建path指定的目录，该参数不能省略
    # os.rmdir(path)  # 删除path指定的目录，该参数不能省略
    # os.listdir(path)  # 列出path目录下所有的文件和目录名
    # os.remove(path)  # 删除path指定的文件，该参数不能省略
    # os.path.isfile(path)  # 判断路径是否为文件
    # os.path.isdir(path)  # 判断路径是否为目录
    # os.path.join(path1[, path2[,]])  # 把目录和文件名合成一个路径

