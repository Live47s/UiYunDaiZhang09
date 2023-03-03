# coding=UTF-8
"""对象包含：1.预收款单里的增删改查 """
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




class Fund_Management_advancereceipt(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/advance receipt/InsertInDatabase.yaml')
    data1 = data[0]['FundsManagement']
    customer = (By.XPATH, data1['customer'])
    customer1 = (By.XPATH, data1['customer1'])
    date = (By.XPATH, data1['date'])
    account = (By.XPATH, data1['account'])
    account1 = (By.XPATH, data1['account1'])
    type = (By.XPATH, data1['type'])
    money = (By.XPATH, data1['money'])
    money1 = (By.XPATH, data1['money1'])
    save= (By.XPATH, data1['save'])
    last = (By.XPATH, data1['last'])
    save1 = (By.XPATH, data1['save1'])
    delete = (By.XPATH, data1['delete'])
    dodelete = (By.XPATH, data1['dodolete'])

    resh= (By.XPATH, data1['resh'])

    # 基础资料 新增预收款单
    def add_advancereceipt(self,advancereceiptName):
        try:

            if advancereceiptName == "UI自动化新增预收款单003":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入客户名称
                self.input(self.customer,'')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入客户名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击输入日期
                self.clear(self.date)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.date,"2022-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入金额
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.money,"10000")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif advancereceiptName == "UI自动化新增预收款单001":
                time.sleep(2)
                # # 点击输入客户名称
                self.input(self.customer,'单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入客户名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advanceReceipt"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择客户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                # 点击输入日期
                self.clear(self.date)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.date,"2022-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.input(self.account,'单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advanceReceipt"]/div[2]/div[4]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 输入金额
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.money,"10000")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(1.5)
                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif advancereceiptName == "UI自动化新增预收款单002":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入客户名称
                self.input(self.customer, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入客户名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advanceReceipt"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择客户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击输入日期
                self.clear(self.date)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.date, "2022-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.account, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advanceReceipt"]/div[2]/div[4]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入金额
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text

                return self.a
        except:

                allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.refresh()
                time.sleep(3)
                return "用例执行失败"


    # 修改
    def change_advancereceipt(self,changeCustomerName):
        try:
            self.click(self.resh)
            time.sleep(2)
                # 点击末张
            self.click(self.last)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击末张",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            if changeCustomerName == '修改预收款单数据01':
                # 输入金额
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.money)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.money, "99999")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.save1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 获取“保存成功”提示弹窗文本
                time.sleep(1.5)
                self.a = self.driver.find_element_by_class_name('el-message').text

                return self.a
            else:
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.money)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.save1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.a = self.driver.find_element_by_class_name('el-message').text
                return self.a


        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败的截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            return "用例执行失败"


    # 基础资料 删除单条客户信息
    def delete_advancereceipt(self,deleteName):
        try:
            self.click(self.resh)
            time.sleep(2)

            self.click(self.last)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击末张",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            self.click(self.delete)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击删除",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.dodelete)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击确定",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            time.sleep(1)
            self.a = self.driver.find_element_by_class_name('el-message').text
            return self.a

        except:
            return "用例失败"



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Fund_Management_advancereceipt(driver)
    # k = lp.add_advancereceipt("UI自动化新增预收款单001")
    # lp.seach_advancereceipt("单个精准查询")
    lp.delete_advancereceipt("删除选手")
    # lp.change_advancereceipt("修改预收款单数据01")

    driver.quit()