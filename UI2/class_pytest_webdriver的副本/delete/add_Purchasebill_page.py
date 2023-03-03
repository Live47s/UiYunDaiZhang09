# # coding=UTF-8
# """登录页面对象包含：1核心页面元素：账号，密码，登录按钮等 2.核心业务流程：入库行为"""
# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
#
# from base.base_page import BasePage
# from config.yamlload import loadyaml
# from page_objeck import login_page
# import allure
# from selenium import webdriver
#
#
# from selenium.webdriver.support.ui import WebDriverWait
# #显式等待条件
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
#
# class Add_Purchasebille(BasePage):
#
#     # 核心元素
#     data = loadyaml('/testData/ysdw.yaml')
#     data1 = data[1]['Purchasebill']
#     # company = (By.XPATH,data1['company'])
#     # uesr = (By.XPATH,data1['ustext'])
#     # pwd = (By.XPATH,data1['pwdtext'])
#     # login_btn = (By.XPATH,data1['lgbttext'])
#     seach = (By.XPATH,data1['seach'])
#     seach1 = (By.XPATH, data1['seach1'])
#     openSelltext = (By.XPATH,data1['openSelltext'])
#     stockmanagement = (By.XPATH,data1['stockmanagement'])
#     purchasOrder = (By.XPATH,data1['purchase order'])
#     ttt = (By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li/span')
#     yyy = (By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li/span')
#     dealers = (By.XPATH,data1['dealers'])
#     # A = (By.XPATH,data1['A'])
#     wuhan =(By.XPATH,data1['wuhan'])
#     warehouse = (By.XPATH,data1['warehouse'])
#     ProductID = (By.XPATH,data1['ProductID'])
#     ProductID2 = (By.XPATH,data1['ProductID2'])
#     product = (By.XPATH, data1['product'])
#     count = (By.XPATH, data1['count'])
#     count1 = (By.XPATH, data1['count1'])
#     warehouse1 = (By.XPATH, data1['warehouse1'])
#     warehouse2 = (By.XPATH,data1['warehouse2'])
#     univalence = (By.XPATH, data1['univalence'])
#     univalence1 = (By.XPATH, data1['univalence1'])
#     save = (By.XPATH, data1['save'])
#     text =(By.XPATH, data1['text'])
#     text1 = (By.XPATH, data1['text1'])
#     businessadministration = (By.XPATH, data1['businessadministration'])
#
#
#
#     # 核心业务流  入库行为
#     def add_Purchasebill(self):
#         # 登录行为
#         self.log = login_page.LgoinPage(driver)
#         self.log1 = self.log.login()
#         # 查询固定的账套点击进入
#         self.input(self.seach,'ui')
#         time.sleep(2)
#         # self.click(self.seach1)
#         # allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}进入账套后",allure.attachment_type.PNG)  # 保存截图为allure的附件
#         # 打开进销存
#         self.click(self.openSelltext)
#         allure.attach(self.driver.get_screenshot_as_png(), f"对{self.openSelltext}打开进销存后",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # 切换窗口 点击采购管理
#         time.sleep(2)
#         self.driver.switch_to.window(self.driver.window_handles[1])
#
#         # self.click(self.stockmanagement)
#         # allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.stockmanagement}点击入库管理",
#         #               allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # # 找到需要悬停的页面元素
#         link1 = driver.find_element(By.XPATH,
#                                     '//*[@id="app"]/div/section/section/div[1]/ul/li[2]/span/span/div/div/div/span')
#         # 模拟鼠标悬停操作
#         action = ActionChains(driver)
#         action.move_to_element(link1).perform()
#         time.sleep(2)
#         # 移动鼠标
#         action.move_by_offset(100, 40).click()
#         action.perform()
#         time.sleep(5)
#
#         # 点击采购订单
#         # self.click(self.purchasOrder)
#         # allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.purchasOrder}点击采购订单",
#         #               allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#
#         # 经销商
#         self.click(self.dealers)
#         self.click(self.ttt)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.ttt}点击经销商",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # 仓库
#         self.click(self.warehouse)
#         self.click(self.yyy)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.yyy}点击仓库",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#
#         # 商品
#         self.click(self.ProductID)
#         self.click(self.ProductID2)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.ProductID2}选择商品",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # self.click(self.product)
#         # 仓库
#         self.click(self.warehouse1)
#         self.click(self.warehouse2)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.warehouse2}设置仓库",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # 数量
#         self.click(self.count)
#         self.input(self.count1,10)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.count}设置数量",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#         # 价格
#         self.click(self.univalence)
#         self.input(self.univalence1,100)
#         self.click(self.univalence)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.univalence}设置价格",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#
#         # 保存
#         self.click(self.save)
#         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.save}点击保存",
#                       allure.attachment_type.PNG)  # 保存截图为allure的附件
#
#
#         time.sleep(2.5)
#         self.a = self.driver.find_element_by_class_name('el-message').text
#         # self.a = str(float(self.a))
#
#
#         return self.a
#
#
#
#
# if __name__ == '__main__':
#     driver =  webdriver.Chrome()
#     w = Add_Purchasebille(BasePage)
#     p = w.add_Purchasebill("嘟嘟嘟")
