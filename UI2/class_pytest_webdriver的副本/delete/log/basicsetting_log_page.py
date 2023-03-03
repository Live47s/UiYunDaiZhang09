# coding=UTF-8
"""日志设置对象包含：1.日志的改查 """
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


class Basic_Setting_log(BasePage):
    # 核心元素
    data = loadyaml('/invertonyDatabase.yaml')
    data1 = data[0]['log']
    startime = (By.XPATH, data1['startime'])
    endtime = (By.XPATH, data1['endtime'])
    input1 = (By.XPATH, data1['input1'])
    seach = (By.XPATH, data1['seach'])
    number1 = (By.XPATH, data1['number1'])
    resh= (By.XPATH, data1['resh'])

    # 基础资料 查询日志信息
    def seach_log(self,queryName):
        try:

            time.sleep(3)
            # 清除查询项
            if queryName == "修改存货,编号是:0013":
                time.sleep(2)

                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.startime, "2022-12-14")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.input(self.endtime,"2022-12-14")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.input1)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除查询内容",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.input1,queryName)
                allure.attach(self.driver.get_screenshot_as_png(), f"输入查询内容",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.seach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(5)

                self.customerNum = self.obtain_value(self.number1)
                return  self.customerNum

            elif queryName == "1999-12-01" :
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.startime, "1999-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.endtime, "2022-12-14")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.input1)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除查询内容",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.seach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.a = self.driver.find_element_by_class_name('el-message').text
                return self.a

            else:
                self.refresh()
                time.sleep(4)
                self.clear(self.startime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.startime, "2022-12-14")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入开始时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.clear(self.endtime)
                allure.attach(self.driver.get_screenshot_as_png(), f"清除结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


                self.input(self.endtime, "2022-12-14")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入结束时间",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.click(self.seach)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击查询",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                time.sleep(3)

                self.customerNum = self.obtain_value(self.number1)
                return self.customerNum
        except:
            self.refresh()
            return "用例失败"







if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting_log(driver)
    # k = lp.add_log("新增账户")
    lp.seach_log("修改存货,编号是:0013")
    # lp.seach_log("日志设置")
    # lp.delete_log("UI自动化新增账户001")
    driver.quit()