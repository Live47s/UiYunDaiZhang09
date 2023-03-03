# coding=UTF-8
"""存货价格设置对象包含：1.存货价格的改查 """
import random
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver
from base.login import Login

import requests
from base import login
from selenium.webdriver.support.ui import WebDriverWait
#显式等待条件
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Fund_Management_paymentlist(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/paymentlist/InsertInDatabase.yaml')
    data1 = data[0]['FundsManagement']
    startime = (By.XPATH, data1['startime'])
    endtime= (By.XPATH, data1['endtime'])
    doseach= (By.XPATH, data1['doseach'])
    resh= (By.XPATH, data1['resh'])
    number= (By.XPATH, data1['number'])
    paymentdate = (By.XPATH, data1['paymentdate'])
    gongyingshang= (By.XPATH, data1['gongyingshang'])
    jiezhangzahnghu= (By.XPATH, data1['jiezhangzahnghu'])
    customer= (By.XPATH, data1['customer'])
    listtype = (By.XPATH, data1['listtype'])
    fukuandan = (By.XPATH, data1['fukuandan'])
    jiezhangzahnghu1 = (By.XPATH, data1['jiezhangzahnghu1'])



    # 基础资料 查询存货价格信息
    def seach_paymentlist(self,queryName):

        self.click(self.resh)
        try:
            if queryName == "UI自动化查询单据001":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime,'2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)
                # 获取数量编码
                self.customerNum = self.obtain_value(self.number)

                return self.customerNum

            elif queryName == "UI自动化查询单据002":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2023-01-04')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-04')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)
                # 获取单据日期
                self.customerNum = self.obtain_value(self.paymentdate)

                return self.customerNum

            elif queryName == "UI自动化查询单据003":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2022-10-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.a = self.driver.find_element_by_class_name('el-message').text

                return self.a

            elif queryName == "UI自动化查询单据004":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.listtype, '付款单')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[2]/div/div[1]/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(2)

                # 获取单据类型
                self.customerNum = self.obtain_value(self.fukuandan)

                return self.customerNum

            elif queryName == "UI自动化查询单据005":

                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.listtype, '收款单')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,
                                                 '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[2]/div/div[1]/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(2)

                # 获取单据类型
                self.customerNum = self.obtain_value(self.fukuandan)
                return self.customerNum


            elif queryName == "UI自动化查询单据006":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.input(self.gongyingshang, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,
                                                 '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[3]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.jiezhangzahnghu, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,
                                                 '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[5]/div/div[1]/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(2)

                # 获取单据类型
                self.customerNum = self.obtain_value(self.jiezhangzahnghu1)
                return self.customerNum


            elif queryName == "UI自动化查询单据007":
                # 清除开始时间
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入开始时间
                self.input(self.startime, '2022-12-15')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 清除结束时间
                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入结束时间
                self.input(self.endtime, '2023-01-05')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.customer, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,
                                                 '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[4]/div/div[1]/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.jiezhangzahnghu, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"单据类型",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,
                                                 '//*[@id="paymentList"]/div[1]/div[1]/div[1]/div[5]/div/div[1]/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击查询
                self.click(self.doseach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(2)

                # 获取单据类型
                self.customerNum = self.obtain_value(self.jiezhangzahnghu1)

                return self.customerNum


        except:
            self.refresh()
            return "用例失败"





if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Fund_Management_paymentlist(driver)
    # # k = lp.add_paymentlist("新增账户")
    # lp.change_paymentlist("存货价格设置")
    # lp.seach_paymentlist("UI自动化查询单据006")
    # lp.delete_paymentlist("UI自动化新增账户001")
    driver.quit()