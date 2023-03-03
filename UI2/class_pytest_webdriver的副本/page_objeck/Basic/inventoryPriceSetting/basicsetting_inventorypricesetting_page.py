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


class Basic_Setting_inventorypricesetting(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/inventoryPriceSetting/InsertInDatabase.yaml')
    data1 = data[0]['inventorypricesetting']
    seach = (By.XPATH, data1['seach'])
    doseach = (By.XPATH, data1['doseach'])
    number = (By.XPATH, data1['number'])
    number1 = (By.XPATH, data1['number1'])
    Update = (By.XPATH, data1['Update'])
    UpdatePrice1 = (By.XPATH, data1['UpdatePrice1'])
    UpdatePrice2 = (By.XPATH, data1['UpdatePrice2'])
    saveUpdate = (By.XPATH, data1['saveUpdate'])
    # checkbox = (By.XPATH, data1['checkbox'])
    # updateAll = (By.XPATH, data1['updateAll'])
    # checkbox1 = (By.XPATH, data1['checkbox1'])
    # # 选择零售价
    # check1 = (By.CLASS_NAME, data1['check1'])
    #
    # # 点击第二个下拉框
    # checkbox2 = (By.XPATH, data1['checkbox2'])
    # # 选择采购价
    # check2 = (By.XPATH, data1['check2'])
    # # 点击第三个下拉框
    # checkbox3 = (By.XPATH, data1['checkbox3'])
    # # 选择+号
    # check3 = (By.XPATH, data1['check3'])
    # # 输入金额
    # inputprice = (By.XPATH, data1['inputprice'])
    # # 确认
    # doUpdate = (By.XPATH, data1['doUpdate'])



    # 基础资料 查询存货价格信息
    def seach_inventorypricesetting(self,queryName):
        try:
            # # 鼠标悬浮到基础设置按钮
            # link1 = self.driver.find_element(By.XPATH,
            #                         '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
            # # 模拟鼠标悬停操作
            # action = ActionChains(self.driver)
            # action.move_to_element(link1).perform()
            # time.sleep(2)
            # # 移动鼠标点击基础资料
            # action.move_by_offset(100, 150).click()
            # action.perform()
            self.refresh()
            time.sleep(3)
            # 清除查询项
            self.clear(self.seach)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seach}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询存货价格的名称
            self.input(self.seach, queryName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{queryName}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.doseach)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(2)
            if queryName == "存货价格设置":
                # 获取“批量模糊查询”总条数
                time.sleep(1)
                self.customerNum = self.obtain_value(self.number1)
                return self.customerNum
            else:
                # 获取“存货价格编码”编码
                time.sleep(1)
                self.customerNum = self.obtain_value(self.number)
                return self.customerNum
        except:
            self.refresh()
            return "用例失败"


    # 基础资料 修改存货价格信息,先查询待修改数据，再修改
    def change_inventorypricesetting(self,UpdateName):
        try:
            # # 鼠标悬浮到基础设置按钮
            # link1 = self.driver.find_element(By.XPATH,
            #                         '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
            # # 模拟鼠标悬停操作
            # action = ActionChains(self.driver)
            # action.move_to_element(link1).perform()
            # time.sleep(2)
            # # 移动鼠标点击基础资料
            # action.move_by_offset(100, 150).click()
            # action.perform()
            self.refresh()
            time.sleep(3)
            # 清除查询项
            self.clear(self.seach)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seach}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 输入查询存货价格的名称
            self.input(self.seach, UpdateName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seach}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.doseach)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.doseach}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # if UpdateName == '存货价格设置':
            #     # 点击全选
            #     self.click(self.checkbox)
            #     #点击批量修改
            #     self.click(self.updateAll)
            #     time.sleep(1)
            #     #点击第一个下拉框
            #     self.click(self.checkbox1)
            #     # 选择零售价
            #     self.click(self.check1)
            #     # 点击第二个下拉框
            #     self.click(self.checkbox2)
            #     # 选择采购价
            #     self.click(self.check2)
            #     # 点击第三个下拉框
            #     self.click(self.checkbox3)
            #     # 选择+号
            #     self.click(self.check3)
            #     # 输入金额
            #     self.input(self.inputprice,6)
            #     #点击确定
            #     self.click(self.doUpdate)
            #     # 获取“修改成功”弹窗文本
            #     self.a = self.driver.find_element_by_class_name('el-message').text
            #     print(self.a)
            #     return self.a
            # else:
                # 点击修改
            self.click(self.Update)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.Update}点击修改",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 清除之前的存货价格
            self.clear(self.UpdatePrice1)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.UpdatePrice1}清除采购价",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 采购价为1-100随机数，销售价为采购价+10
            purchasePrice = random.randint(1,100)
            salesPrice = purchasePrice+10

            # 输入采购价
            self.input(self.UpdatePrice1,purchasePrice)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.UpdatePrice1}输入采购价",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 清除之前的存货价格
            self.clear(self.UpdatePrice2)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.UpdatePrice2}清除销售价",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 输入销售价
            self.input(self.UpdatePrice2,salesPrice)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.UpdatePrice2}输入销售价",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.saveUpdate)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.saveUpdate}点击保存",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 获取“保存成功”提示弹窗文本
            self.a = self.driver.find_element_by_class_name('el-message').text
            return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"{self.saveUpdate}用例失败的截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            return "用例执行失败"






if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting_inventorypricesetting(driver)
    # k = lp.add_inventorypricesetting("新增账户")
    lp.change_inventorypricesetting("存货价格设置")
    # lp.seach_inventorypricesetting("存货价格设置")
    # lp.delete_inventorypricesetting("UI自动化新增账户001")
    driver.quit()