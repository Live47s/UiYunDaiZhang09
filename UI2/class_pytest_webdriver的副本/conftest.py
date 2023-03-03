import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.login import Login
from url import base_url


global environment
environment = '生产环境'
# 基础设置
setting = '//*[@id="app"]/div/section/section/div[1]/ul/li[7]/span/span/div/div/div/span'
online_setting = '//*[@id="app"]/div/section/section/div[1]/ul/li[7]/span/span/div/div/div/span'
# 资金管理
advance = '//*[@id="app"]/div/section/section/div[1]/ul/li[5]/span/span/div/div/div/span'
online_advance = '//*[@id="app"]/div/section/section/div[1]/ul/li[5]/span/span/div/div/div/span'


# driver = None
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    # 添加allure报告截图
    if rep.when == 'call' and rep.failed:
        img = driver.get_screenshot_as_png()
        allure.attach(img,"失败截图",allure.attachment_type.PNG)


# 登录，退出登录
@pytest.fixture(scope='session',autouse=True)
def init_driver(*loc):
    """打开Safari浏览器"""
    global driver
    # 打开Safari浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # 隐式等待
    driver.implicitly_wait(10)
    # 窗口最大化
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # 设置测试环境还是正式环境
    # 调用登录函数
    if environment == '生产环境':
        a = Login(driver)
        a.login2()
    elif environment == '测试环境':
        a = Login(driver)
        a.login1()
    # 区分前后置
    yield driver
    """退出Safari浏览器"""
    # 等待2S
    time.sleep(2)
    # 退出浏览器
    driver.quit()
    return driver

# 进入基础设置-客户页面
@pytest.fixture(scope='class',autouse=False ,name='setting')
def basic_customer():
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                         online_setting)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,setting
                                    )
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击基础资料
    action.move_by_offset(100, 40).click()
    action.move_by_offset(100, 40).click()
    action.perform()

# 进入基础设置-存货价格设置页面
@pytest.fixture(scope='class',autouse=False ,name='inventoryPrice')
def inventoryPrice():
    time.sleep(3)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                         online_setting)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    setting)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 150).click()
    action.move_by_offset(100, 150).click()
    action.perform()
    time.sleep(3)

# 进入基础设置-客户价格设置页面
@pytest.fixture(scope='class',autouse=False ,name='customerPrice')
def customerPrice():
    driver.refresh()
    time.sleep(5)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                         online_setting)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    setting)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 120).click()
    action.move_by_offset(100, 120).click()
    action.perform()
    time.sleep(3)

# 进入基础设置-日志页面
@pytest.fixture(scope='class',autouse=False ,name='log')
def log():
    time.sleep(3)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    online_setting)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    setting)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 90).click()
    action.move_by_offset(100, 90).click()
    action.perform()
    time.sleep(3)


# 进入资金管理 - 预收款单页面
@pytest.fixture(scope='class',autouse=False ,name='AdvanceReceipt')
def AdvanceReceipt():
    time.sleep(3)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    online_advance)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    advance)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 120).click()
    action.move_by_offset(100, 120).click()
    action.perform()
    time.sleep(3)


# 进入资金管理 - 预付款单页面
@pytest.fixture(scope='class',autouse=False ,name='AdvancePayment')
def AdvancePayment():
    time.sleep(3)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                         online_advance)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    advance)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 150).click()
    action.move_by_offset(100, 150).click()
    action.perform()
    time.sleep(3)


# 进入资金管理 - 付款单页面
@pytest.fixture(scope='class', autouse=False, name='Billofpayment')
def Billofpayment():
    time.sleep(3)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    online_advance)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    advance)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 30).click()
    action.move_by_offset(100, 30).click()
    action.perform()
    time.sleep(3)


# 进入资金管理 - 收款单页面
@pytest.fixture(scope='class', autouse=False, name='Receipt')
def Receipt():
    time.sleep(3)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    online_advance)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    advance)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(100, 90).click()
    action.move_by_offset(100, 90).click()
    action.perform()
    time.sleep(3)


# 进入资金管理 - 财务单据列表
@pytest.fixture(scope='class', autouse=False, name='PaymentList')
def PaymentList():
    time.sleep(3)
    print(environment)
    if environment == '生产环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    online_advance)
    elif environment == '测试环境':
        # 鼠标悬浮到基础设置按钮
        driver.implicitly_wait(10)
        link1 = driver.find_element(By.XPATH,
                                    advance)
    # 模拟鼠标悬停操作
    action = ActionChains(driver)
    action.move_to_element(link1).perform()
    time.sleep(1)
    # 移动鼠标点击存货价格设置
    action.move_by_offset(200, 30).click()
    action.move_by_offset(200, 30).click()
    action.perform()
    time.sleep(3)


# # 基础设置 - 基础资料 - 新增自定义项目
# @pytest.fixture(scope='class',autouse=False ,name='addnewuserdefined')
# def addnewuserdefined():
#     try:
#         # 点击新增
#         driver.find_element(By.CLASS_NAME,'Addplus').click()
#         # 输入名称
#         driver.find_element(By.XPATH,'//*[@id="Newcategory"]/div/div/div[2]/div/div/input').send_keys('UI自动化')
#         # 点击确定
#         driver.find_element(By.XPATH,'//*[@id="Newcategory"]/div/div/div[3]/span/button[2]/span')
#
#         yield driver
#         # 定位到新增的自定义项目
#         driver.find_element(By.XPATH,'//*[@id="tab-AuxiliaryAttributes"]/../div[12]/span/span/span/span').click()
#         # 点击删除
#         driver.find_element(By.XPATH, '//*[@class="el-popover el-popper popoverStyle"]/../div/span[2]').click()
#         # 点击确定
#         driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span').click()
#     except:/html/body/div[3]/div[1]/div[1]/ul
#         driver.refresh()
#         time.sleep(10)
#         # 定位到新增的自定义项目
#         driver.find_element(By.XPATH, '//*[@id="tab-AuxiliaryAttributes"]/../div[12]/span/span/span/span').click()
#         # 点击删除
#         driver.find_element(By.XPATH, '//*[@class="el-popover el-popper popoverStyle"]/../div/span[2]').click()
#         # 点击确定
#         driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span').click()
#         yield driver
#         # 定位到新增的自定义项目
#         driver.find_element(By.XPATH, '//*[@id="tab-AuxiliaryAttributes"]/../div[12]/span/span/span/span').click()
#         # 点击删除
#         driver.find_element(By.XPATH, '//*[@class="el-popover el-popper popoverStyle"]/../div/span[2]').click()
#         # 点击确定
#         driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span').click()
