# coding=UTF-8
"""基础设置对象包含：1.基础资料里客户的增删改查 """
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


@pytest.mark.usefixtures('basic_customer')


class Basic_Setting(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/customer/InsertInDatabase.yaml')
    data1 = data[1]['BasicSetting']

    stockmanagement = (By.XPATH,data1['stockmanagement'])
    businessadministration = (By.XPATH, data1['businessadministration'])
    basicsetting = (By.XPATH,data1['basicsetting'])
    basedata = (By.XPATH, data1['basedata'])
    customer = (By.ID, data1['customer'])
    # 增
    addnewcustomer = (By.XPATH, data1['addnewcustomer'])
    newcustomername = (By.XPATH, data1['newcustomername'])

    # 保存
    savecustomer = (By.XPATH, data1['savecustomer'])
    # 取消
    cancel = (By.XPATH, data1['cancel'])

    # 改
    changecustomer = (By.XPATH, data1['changecustomer'])

    # 查
    seachcustomer = (By.XPATH, data1['seachcustomer'])
    seach2 = (By.XPATH, data1['seach2'])
    getcustomername = (By.XPATH, data1['getcustomername'])
    getcustomerPage = (By.XPATH, data1['getcustomerPage'])

    # 删
    deletecustomer = (By.XPATH, data1['deletecustomer'])
    dodelete = (By.XPATH, data1['dodelete'])
    deleteparmisnull= (By.XPATH, data1['deleteparmisnull'])


    # 第四个客户的复选框
    # lastcustomername = (By.XPATH, data1['lastcustomername'])

    # 刷新
    refresh1 = (By.XPATH, data1['refresh'])
    test111 = (By.XPATH, data1['test111'])




    # 基础资料 新增客户
    def add_Customer(self,customerName):
        # a = Login(driver)
        # a.login1()
        # # 鼠标悬浮到基础设置按钮
        # link1 = self.driver.find_element(By.XPATH,
        #                                  '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
        # # 模拟鼠标悬停操作
        # action = ActionChains(self.driver)
        # action.move_to_element(link1).perform()
        # time.sleep(2)
        # # 移动鼠标点击基础资料
        # action.move_by_offset(100, 40).click()
        # action.perform()
        # driver.implicitly_wait(10)
        try:
            # 点击客户按钮
            self.click(self.customer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.customer}客户",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击新增
            time.sleep(2)
            # try:
            self.click(self.addnewcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",allure.attachment_type.PNG)  # 保存截图为allure的附件
            # except Exception:
            #     addnewcustomer = self.driver.find_element(By.XPATH,'//*[@id="clientMain"]/div[1]/div[2]/button[3]/span')
            #     self.click(addnewcustomer)


            self.input(self.newcustomername,customerName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件.


            # 返回
            self.a = self.driver.find_element_by_class_name('el-message').text
            self.refresh()
            time.sleep(2)
            return self.a

        # # 获取“请求成功”提示弹窗文本
        # if customerName == "名称重复客户":
        #     #   class ="el-message el-message--warning"
        #
        #
        #
        # elif customerName == "UI自动化新增用户001":
        #     # class ="el-message el-message--success"
        #     self.a = self.driver.find_element_by_class_name('el-message').text
        #     return self.a

        # else:
        #     # 点击保存
        #     self.click(self.savecustomer)
        #     allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
        #                   allure.attachment_type.PNG)  # 保存截图为allure的附件
        #     self.a = self.driver.find_element_by_class_name('el-message').text
        #     print(self.a)
        #     self.refresh()
        #     return self.a
        except:

                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击取消的截图",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.refresh()
                return "用例执行失败"


    # 基础资料 修改客户信息,先查询待修改数据，再修改
    def change_Customer(self,changeCustomerName):
        try:
            # a = Login(driver)
            # a.login1()
            # self.refresh()
            # time.sleep(2)
            # # 鼠标悬浮到基础设置按钮
            # link1 = self.driver.find_element(By.XPATH,
            #                                  '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
            # # 模拟鼠标悬停操作
            # action = ActionChains(self.driver)
            # action.move_to_element(link1).perform()
            # time.sleep(2)
            # # 移动鼠标点击基础资料
            # action.move_by_offset(100, 40).click()
            # action.perform()
            #
            time.sleep(2)
            # driver.implicitly_wait(10)

            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, "修改客户")
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击修改
            self.click(self.changecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.changecustomer}点击修改",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 清除之前的客户名称
            self.clear(self.newcustomername)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.newcustomername}清除客户名",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入客户名称

            changetTime = time.strftime('%Y/%m/%d-%H:%M')
            changename = changeCustomerName + changetTime


            self.input(self.newcustomername, changename)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            if changeCustomerName == "修改客户数据":
                # 获取“请求成功”提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message').text
                self.refresh()
                time.sleep(2)
                return self.a
            else:
                self.a = self.driver.find_element_by_class_name('el-message').text
                self.b = self.driver.find_element_by_class_name('el-message--warning').text
                self.refresh()
                time.sleep(3)
                if self.a == "":
                    return self.b
                else:return  self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击取消的截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(2)
            return "用例执行失败"


    # 基础资料 查询客户信息
    def seach_Customer(self,queryName):
        try:
            # a = Login(driver)
            # a.login1()
            self.refresh()
            time.sleep(2)
            # # 鼠标悬浮到基础设置按钮
            # link1 = self.driver.find_element(By.XPATH,
            #                         '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
            # # 模拟鼠标悬停操作
            # action = ActionChains(self.driver)
            # action.move_to_element(link1).perform()
            # time.sleep(2)
            # # 移动鼠标点击基础资料
            # action.move_by_offset(100, 40).click()
            # action.perform()
            #
            # time.sleep(2)

            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, queryName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{queryName}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(2)
            if queryName == "批量模糊查询":
                # 获取“批量模糊查询”总条数
                time.sleep(1)
                self.customerNum = self.obtain_value(self.getcustomerPage)
                return self.customerNum
            else:

                # 获取“客户编码”文本
                time.sleep(1)
                self.customerNum = self.obtain_value(self.getcustomername)
                return self.customerNum
        except:
            self.refresh()
            time.sleep(2)
            return "用例失败"

    # 基础资料 删除单条客户信息
    def delete_Customer(self,deleteName):
        try:
            # a = Login(driver)
            # a.login1()
            self.refresh()
            time.sleep(2)
            # # 鼠标悬浮到基础设置按钮
            # link1 = self.driver.find_element(By.XPATH,
            #                                  '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
            # # 模拟鼠标悬停操作
            # action = ActionChains(self.driver)
            # action.move_to_element(link1).perform()
            # time.sleep(2)
            # # 移动鼠标点击基础资料
            # action.move_by_offset(100, 40).click()
            # action.perform()
            #
            # time.sleep(2)

            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, "UI自动化新增用户001")
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(2)
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(2)
            # 若无新建数据，则先新增数据，查询后，再删除。
            try:
                if self.obtain_value(self.deleteparmisnull) == "暂无数据":
                    # 点击新增
                    time.sleep(1)
                    try:
                        self.click(self.addnewcustomer)
                        allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",
                                      allure.attachment_type.PNG)  # 保存截图为allure的附件
                    except Exception:
                        addnewcustomer = self.driver.find_element(By.XPATH,
                                                                  '//*[@id="clientMain"]/div[1]/div[2]/button[3]/span')
                        self.click(addnewcustomer)

                    self.input(self.newcustomername, deleteName)
                    allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    # 点击保存
                    self.click(self.savecustomer)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    # 清除查询项
                    self.clear(self.seachcustomer)
                    allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件

                    # 输入查询客户的名称
                    self.input(self.seachcustomer, deleteName)
                    allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    # 点击查询
                    self.click(self.seach2)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件

                    self.click(self.deletecustomer)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.deletecustomer}点击删除",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    time.sleep(1)
                    # 点击确定删除
                    self.click(self.dodelete)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.dodelete}点击确定删除",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件

                    time.sleep(2)
                    return self.obtain_value(self.deleteparmisnull)

            except:
                # 点击删除
                self.click(self.deletecustomer)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.deletecustomer}点击删除",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(1)
                # 点击确定删除
                self.click(self.dodelete)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.dodelete}点击确定删除",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)
                return self.obtain_value(self.deleteparmisnull)






            # self.click(self.seach2)
            # allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
            #               allure.attachment_type.PNG)  # 保存截图为allure的附件
            #
            # # 刷新页面数据
            # self.click(self.refresh1)
            # allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.refresh1}点击刷新",
            #               allure.attachment_type.PNG)  # 保存截图为allure的附
            # time.sleep(1)
            #
            # # 获取客户名称列表里的最后一个客户名称和changename对比
            # self.customername = []
            # for i in range(1, 50):
            #     try:
            #         self.customername = list(self.customername)
            #         self.text = ('xpath', '//*[@id="clientMain"]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[' + str(
            #             i) + ']/td[3]/div')
            #         self.a = self.obtain_value(self.text)
            #         self.customername.append(self.a)
            #     except:
            #         pass
            #
            # self.a = self.customername[0]
            # time.sleep(1)
            # return self.a
        except:
            return "用例失败"



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting(driver)
    k = lp.add_Customer("名称重复客户")
    # lp.change_Customer("名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户名称重复客户")
    # lp.seach_Customer("单个精准查询")
    # lp.delete_Customer("删除选手")
    driver.quit()