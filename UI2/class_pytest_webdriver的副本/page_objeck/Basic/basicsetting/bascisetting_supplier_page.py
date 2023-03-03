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



class Basic_Setting_Supplier(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/supplier/supplierDatabase.yaml')
    data1 = data[1]['BasicSetting']
    Supplier = (By.ID,data1['Supplier'])
    stockmanagement = (By.XPATH,data1['stockmanagement'])
    businessadministration = (By.XPATH, data1['businessadministration'])
    basicsetting = (By.XPATH,data1['basicsetting'])
    basedata = (By.XPATH, data1['basedata'])

    # 增
    addnewcustomer = (By.XPATH, data1['addnewcustomer'])
    newcustomername = (By.XPATH, data1['newcustomername'])
    savecustomer = (By.XPATH, data1['savecustomer'])

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


    # 基础资料 新增供应商
    def add_Supplier(self,supplierName):
        try:
            # a = Login(driver)
            # a.login1()
            # time.sleep(2)
            # self.refresh()
            # driver.implicitly_wait(10)

            # 点击进入供应商页面
            self.click(self.Supplier)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.Supplier}点击新增",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击新增
            time.sleep(2)
            try:
                self.click(self.addnewcustomer)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",allure.attachment_type.PNG)  # 保存截图为allure的附件
            except Exception:
                addnewcustomer = self.driver.find_element(By.XPATH,'//*[@id="supplierMain"]/div[1]/div[2]/button[3]/span')
                self.click(addnewcustomer)


            self.input(self.newcustomername,supplierName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件


            # 获取“请求成功”提示弹窗文本
            if supplierName == "名称重复用户":
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a
            elif supplierName == "UI自动化新增用户001":
                self.a = self.driver.find_element_by_class_name('el-message').text
                return self.a
            else:
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()

            return "用例执行失败"


    # 基础资料 修改供应商信息,先查询待修改数据，再修改
    def change_Supplier(self,changeSupplierName):
        try:
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

            # 点击进入供应商页面
            self.click(self.Supplier)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.Supplier}点击新增",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件


            time.sleep(2)
            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询供应商的名称
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
            changename = changeSupplierName + changetTime
            self.input(self.newcustomername, changename)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 获取“请求成功”提示弹窗文本
            time.sleep(1)
            self.a = self.driver.find_element_by_class_name('el-message').text
            self.refresh()
            time.sleep(3)
            # print(self.a)
            return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(2)
            return "用例执行失败"


    # 基础资料 查询客户信息
    def seach_Supplier(self,queryName):
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

            # 点击进入供应商页面
            self.click(self.Supplier)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.Supplier}点击新增",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件


            time.sleep(2)
            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            time.sleep(2)
            self.input(self.seachcustomer, queryName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{queryName}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(1)
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
            time.sleep(1)
            return "用例失败"

    # 基础资料 删除单条客户信息
    def delete_Supplier(self,deleteName):
        try:
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

            self.refresh()
            time.sleep(2)
            # 点击进入供应商页面
            self.click(self.Supplier)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.Supplier}点击新增",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            time.sleep(2)
            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, "UI自动化新增用户001")
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

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

                # 点击确定删除
                self.click(self.dodelete)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.dodelete}点击确定删除",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)
                return self.obtain_value(self.deleteparmisnull)

        except:
            self.refresh()
            time.sleep(2)
            return "用例失败"



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting_Supplier(driver)
    # k = lp.add_Supplier("3231")
    # lp.change_Supplier("修改供应商")
    # lp.seach_Supplier("单个精准查询")
    lp.delete_Supplier("删除选手")
    driver.quit()