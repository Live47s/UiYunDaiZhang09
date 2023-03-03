# coding=UTF-8
"""基础设置对象包含：1.基础资料里项目的增删改查 """
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver
from base.login import Login




class Basic_Setting_project(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/project/invertonyDatabase.yaml')
    data1 = data[1]['BasicSetting']
    project = (By.ID,data1['project'])
    project1 = (By.ID, data1['project1'])
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
    changenameinput = (By.XPATH, data1['changenameinput'])
    savechangeinput = (By.XPATH, data1['savechangeinput'])

    # 查
    seachcustomer = (By.XPATH, data1['seachcustomer'])
    seach2 = (By.XPATH, data1['seach2'])
    getcustomername = (By.XPATH, data1['getcustomername'])
    getcustomerPage = (By.XPATH, data1['getcustomerPage'])

    # 删
    deletecustomer = (By.XPATH, data1['deletecustomer'])
    dodelete = (By.XPATH, data1['dodelete'])
    dodelete2 = (By.XPATH, data1['dodelete2'])
    deleteparmisnull= (By.XPATH, data1['deleteparmisnull'])


    # 第四个客户的复选框
    # lastcustomername = (By.XPATH, data1['lastcustomername'])

    # 刷新
    refresh1 = (By.XPATH, data1['refresh'])
    test111 = (By.XPATH, data1['test111'])


    # 基础资料 新增项目
    def add_project(self,projectName):
        try:
        #     a = Login(driver)
        #     a.login1()
        #     time.sleep(2)
        #     # 鼠标悬浮到基础设置按钮
        #     link1 = self.driver.find_element(By.XPATH,
        #                                      '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
        #     # 模拟鼠标悬停操作
        #     action = ActionChains(self.driver)
        #     action.move_to_element(link1).perform()
        #     time.sleep(2)
        #     # 移动鼠标点击基础资料
        #     action.move_by_offset(100, 40).click()
        #     action.perform()

            # # 判断环境，点击进入项目页面

            time.sleep(5)
            env = self.obtain_url()
            if 'psi.yundaizhang.com.cn' in str(env):
                self.driver.implicitly_wait(10)
                self.click(self.project1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project1}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.project)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


            # 点击新增
            time.sleep(2)
            try:
                self.click(self.addnewcustomer)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",allure.attachment_type.PNG)  # 保存截图为allure的附件
            except Exception:
                addnewcustomer = self.driver.find_element(By.XPATH,'//*[@id="clientMain"]/div[1]/div[2]/button[1]/span')
                self.click(addnewcustomer)

            self.input(self.newcustomername,projectName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savechangeinput}点击保存",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 获取“请求成功”提示弹窗文本
            if projectName == "名称重复项目":
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                self.refresh()
                return self.a
            elif projectName == "UI自动化新增项目001":
                self.a = self.driver.find_element_by_class_name('el-message').text
                self.refresh()
                return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            return "用例执行失败"


    # 基础资料 修改项目信息,先查询待修改数据，再修改
    def change_project(self,changeprojectName):
        try:
            time.sleep(5)
            # # 判断环境，点击进入项目页面
            env = self.obtain_url()
            if 'psi.yundaizhang.com.cn' in str(env):
                self.driver.implicitly_wait(10)
                self.click(self.project1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project1}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.project)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件


            time.sleep(2)

            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询供应商的名称
            self.input(self.seachcustomer, "修改项目")
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
            self.clear(self.changenameinput)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.changenameinput}清除客户名",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件


            if changeprojectName == "修改项目数据":
                # 输入客户名称
                changetTime = time.strftime('%Y/%m/%d-%H:%M')
                changename = changeprojectName + changetTime
                self.input(self.changenameinput, changename)
                allure.attach(self.driver.get_screenshot_as_png(), f"输入{changename}输入客户名",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击保存
                self.click(self.savechangeinput)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savechangeinput}点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 获取“请求成功”提示弹窗文本
                time.sleep(1)
                self.a = self.driver.find_element_by_class_name('el-message').text
                time.sleep(3)
                # print(self.a)
                return self.a
            # 名称重复
            else:
                self.input(self.changenameinput, changeprojectName)
                allure.attach(self.driver.get_screenshot_as_png(), f"输入{changeprojectName}输入客户名",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                # 点击保存
                self.click(self.savechangeinput)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savechangeinput}点击保存",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.a = self.driver.find_element_by_class_name('el-message__content').text
                # 已存在相同编码或名称与规格的商品！
                return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(2)
            return "用例执行失败"


    # 基础资料 查询项目信息
    def seach_project(self,queryName):
        try:


            self.refresh()
            time.sleep(5)

            # # 判断环境，点击进入项目页面
            env = self.obtain_url()
            if 'psi.yundaizhang.com.cn' in str(env):
                self.driver.implicitly_wait(10)
                self.click(self.project1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project1}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.project)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project}点击新增",
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

    # 基础资料 删除单条项目信息
    def delete_project(self,deleteName):
        try:

            # a = Login(driver)
            # a.login1()
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


            self.refresh()
            time.sleep(5)
            # # 判断环境，点击进入项目页面
            env = self.obtain_url()
            if 'psi.yundaizhang.com.cn' in str(env):
                self.driver.implicitly_wait(10)
                self.click(self.project1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project1}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.project)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.project}点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(2)


            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, "UI自动化新增项目001")
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击查询
            self.click(self.seach2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 若无新建数据，则先新增数据，查询后，再删除。
            try:
                time.sleep(1)
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
                if self.obtain_value(self.deleteparmisnull) == "暂无数据":
                    # 点击新增
                    time.sleep(2)
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
            self.refresh()
            time.sleep(2)
            return "用例失败"



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting_project(driver)


    # lp.change_project("名称重复项目")
    # lp.change_project("修改项目数据")
    # lp.add_project("名称重复项目")
    # lp.add_project("UI自动化新增项目00121")
    # lp.seach_project("单个精准查询")
    # lp.seach_project("单个模糊")
    # lp.seach_project("批量模糊查询")
    lp.delete_project("UI自动化新增项目001")
    # lp.delete_project("名称重复项目")

    driver.quit()