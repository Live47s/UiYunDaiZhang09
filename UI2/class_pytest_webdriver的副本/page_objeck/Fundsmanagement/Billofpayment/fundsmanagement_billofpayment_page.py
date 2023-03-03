# coding=UTF-8
"""对象包含：1.付款单里的增删改查 """
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




class Fund_Management_billofpayment(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/bill of payment/InsertInDatabase.yaml')
    data1 = data[0]['FundsManagement']
    gongyingshang= (By.XPATH, data1['gongyingshang'])
    date= (By.XPATH, data1['data'])
    account= (By.XPATH, data1['account'])
    money1 = (By.XPATH, data1['money1'])
    money= (By.XPATH, data1['money'])
    zidonghexiao= (By.XPATH, data1['zidonghexiao'])
    save= (By.XPATH, data1['save'])
    resh= (By.XPATH, data1['resh'])
    hexiaomoney= (By.XPATH, data1['hexiaomoney'])
    last = (By.XPATH, data1['last'])
    change= (By.XPATH, data1['change'])
    save1 =  (By.XPATH, data1['save1'])
    delete = (By.XPATH, data1['delete'])
    dodelete= (By.XPATH, data1['dodelete'])


    # 基础资料 新增付款单
    def add_billofpayment(self,billofpaymentName):
        try:

            if billofpaymentName == "UI自动化新增付款单003":

                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.gongyingshang,'')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击输入日期
                self.clear(self.date)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.date,"2022-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 选择账户
                self.input(self.account, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[5]/div/div/input')
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

                self.input(self.money,"100")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.zidonghexiao)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击自动核销",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(1)

                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件



                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif billofpaymentName == "UI自动化新增付款单001":
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.gongyingshang,'单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择供应商",
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[5]/div/div/input')
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

                self.input(self.money,"10")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.zidonghexiao)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击自动核销",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(1)
                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(1.5)

                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif billofpaymentName == "UI自动化新增付款单002":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.gongyingshang, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择供应商",
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[5]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 输入金额时不输入
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 自动核销
                self.click(self.zidonghexiao)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击自动核销",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text

                return self.a

            elif billofpaymentName == "UI自动化新增付款单004":


                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.gongyingshang, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择供应商",
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[5]/div/div/input')
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

                self.input(self.money, "10")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                time.sleep(1)
                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif billofpaymentName == "UI自动化新增付款单005":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.gongyingshang, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[2]/div/div/input')
                action.move_to_element(link1).perform()
                time.sleep(1)
                # 移动鼠标点击存货价格设置
                action.move_by_offset(0, 30).click()
                action.perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择供应商",
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div[2]/div[5]/div/div/input')
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

                self.input(self.money, "10")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.hexiaomoney)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击核销金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.hexiaomoney,'1234')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入核销金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(1)
                # 点击保存
                self.click(self.save)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                print(self.a)
                return self.a

        except:

                allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.refresh()
                time.sleep(3)
                return "用例执行失败"


    # 修改
    def change_billofpayment(self,changegongyingshangName):

        try:
            self.click(self.resh)
            time.sleep(2)
                # 点击末张
            self.click(self.last)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击末张",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            if changegongyingshangName == '修改付款单数据01':

                # 点击修改
                self.click(self.change)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 输入金额
                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.money)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.money, "99")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.zidonghexiao)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击自动核销",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.click(self.save1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 获取“保存成功”提示弹窗文本
                time.sleep(1.5)
                self.a = self.driver.find_element_by_class_name('el-message').text

                return self.a
            else:
                # 点击修改
                self.click(self.change)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.click(self.money1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.money)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空金额",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.zidonghexiao)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击自动核销",
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


    # 基础资料 删除单条供应商信息
    def delete_billofpayment(self,deleteName):

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
    lp = Fund_Management_billofpayment(driver)
    # k = lp.add_billofpayment("UI自动化新增付款单005")
    # lp.seach_billofpayment("单个精准查询")
    lp.delete_billofpayment("删除选手")
    # lp.change_billofpayment("修改付款单数据02")

    driver.quit()