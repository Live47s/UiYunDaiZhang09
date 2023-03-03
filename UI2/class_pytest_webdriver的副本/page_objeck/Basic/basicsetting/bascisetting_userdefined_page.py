# coding=UTF-8
"""基础设置对象包含：1.基础资料里自定义项目的增删改查 """
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver
from base.login import Login




class Basic_Setting_userdefined(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/BaseData/userdefined/InsertInDatabase.yaml')
    data1 = data[0]['BasicSetting']
    stockmanagement = (By.XPATH,data1['stockmanagement'])

    basicsetting = (By.XPATH,data1['basicsetting'])
    basedata = (By.XPATH, data1['basedata'])
    # 新增自定义按钮
    Addplus = (By.CLASS_NAME,data1['Addplus'])
    userdefinedname = (By.XPATH, data1['userdefinedname'])
    addNewcategory = (By.XPATH, data1['addNewcategory'])

    # 增
    addnewcustomer = (By.XPATH, data1['addnewcustomer'])
    newcustomername = (By.XPATH, data1['newcustomername'])
    savecustomer = (By.XPATH, data1['savecustomer'])

    # # 改
    # changecustomer = (By.XPATH, data1['changecustomer'])
    # changenameinput = (By.CSS_SELECTOR, data1['changenameinput'])
    # savechangeinput = (By.CSS_SELECTOR, data1['savechangeinput'])
    #
    # # 查
    seachcustomer = (By.XPATH, data1['seachcustomer'])
    seach2 = (By.XPATH, data1['seach2'])
    # getcustomername = (By.XPATH, data1['getcustomername'])
    # getcustomerPage = (By.XPATH, data1['getcustomerPage'])
    #
    # 删
    deletecustomer = (By.XPATH, data1['deletecustomer'])
    dodelete = (By.XPATH, data1['dodelete'])
    # dodelete2 = (By.XPATH, data1['dodelete2'])
    deleteparmisnull= (By.XPATH, data1['deleteparmisnull'])


    # 第四个客户的复选框
    # lastcustomername = (By.XPATH, data1['lastcustomername'])

    # # 刷新
    # refresh1 = (By.XPATH, data1['refresh'])
    # test111 = (By.XPATH, data1['test111'])

    # 基础设置 - 基础资料 - 新增自定义项目
    # 基础资料 新增自定义项目
    def add_userdefined(self,userdefinedName):
        try:
        # 点击进入自定义项目页面
            link1 = self.driver.find_element(By.ID,'tab-auxiliaryDatum')
            # 模拟鼠标悬停操作
            action = ActionChains(self.driver)
            action.move_to_element(link1).perform()
            time.sleep(1)
            # 移动鼠标点击UI自动化
            action.move_by_offset(120, 0).click()
            action.perform()


            # 点击新增
            time.sleep(2)
            try:
                self.click(self.addnewcustomer)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",allure.attachment_type.PNG)  # 保存截图为allure的附件
            except Exception:
                addnewcustomer = self.driver.find_element(By.XPATH,'//*[@id="commodityMain"]/div[1]/div[2]/button[3]/span')
                self.click(addnewcustomer)

            self.input(self.newcustomername,userdefinedName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.newcustomername}输入客户名",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 点击保存
            self.click(self.savecustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savecustomer}点击保存",
                      allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 获取“请求成功”提示弹窗文本
            if userdefinedName == "名称重复自定义项目人员":
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                self.refresh()
                return self.a
            elif userdefinedName == "UI自动化新增自定义项目人员":
                self.a = self.driver.find_element_by_class_name('el-message').text
                print(self.a)
                self.refresh()
                return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            return "用例执行失败"


    # # 基础资料 修改自定义项目信息,先查询待修改数据，再修改
    # def change_userdefined(self,changeuserdefinedName):
    #     try:
    #         # a = Login(driver)
    #         # a.login1()
    #         # time.sleep(2)
    #         # # 鼠标悬浮到基础设置按钮
    #         # link1 = self.driver.find_element(By.XPATH,
    #         #                                  '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
    #         # # 模拟鼠标悬停操作
    #         # action = ActionChains(self.driver)
    #         # action.move_to_element(link1).perform()
    #         # time.sleep(2)
    #         # # 移动鼠标点击基础资料
    #         # action.move_by_offset(100, 40).click()
    #         # action.perform()
    #
    #         # 点击进入自定义项目页面
    #         self.click(self.userdefined)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.userdefined}点击新增",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #         time.sleep(2)
    #
    #         # 清除查询项
    #         self.clear(self.seachcustomer)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #         # 输入查询供应商的名称
    #         self.input(self.seachcustomer, "修改自定义项目")
    #         allure.attach(self.driver.get_screenshot_as_png(), f"输入{self.seachcustomer}输入查询信息",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #         # 点击查询
    #         self.click(self.seach2)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #         # 点击修改
    #         self.click(self.changecustomer)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.changecustomer}点击修改",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #
    #         # 清除之前的客户名称
    #         self.clear(self.changenameinput)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.changenameinput}清除客户名",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #
    #         if changeuserdefinedName == "修改自定义项目数据":
    #             # 输入客户名称
    #             changetTime = time.strftime('%Y/%m/%d-%H:%M')
    #             changename = changeuserdefinedName + changetTime
    #             self.input(self.changenameinput, changename)
    #             allure.attach(self.driver.get_screenshot_as_png(), f"输入{changename}输入客户名",
    #                           allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #             # 点击保存
    #             self.click(self.savechangeinput)
    #             allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savechangeinput}点击保存",
    #                           allure.attachment_type.PNG)  # 保存截图为allure的附件
    #             # 获取“请求成功”提示弹窗文本
    #             time.sleep(1)
    #             self.a = self.driver.find_element_by_class_name('el-message').text
    #             time.sleep(3)
    #             # print(self.a)
    #             return self.a
    #         # 名称重复
    #         else:
    #             self.input(self.changenameinput, changeuserdefinedName)
    #             allure.attach(self.driver.get_screenshot_as_png(), f"输入{changeuserdefinedName}输入客户名",
    #                           allure.attachment_type.PNG)  # 保存截图为allure的附件
    #             # 点击保存
    #             self.click(self.savechangeinput)
    #             allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.savechangeinput}点击保存",
    #                           allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #             self.a = self.driver.find_element_by_class_name('el-message__content').text
    #             # 已存在相同编码或名称与规格的商品！
    #             return self.a
    #     except:
    #         allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #         self.refresh()
    #         time.sleep(2)
    #         return "用例执行失败"
    #
    #
    # # 基础资料 查询自定义项目信息
    # def seach_userdefined(self,queryName):
    #     try:
    #         self.refresh()
    #         time.sleep(2)
    #
    #
    #         # 点击进入自定义项目页面
    #         self.click(self.userdefined)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.userdefined}点击新增",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #         time.sleep(2)
    #
    #         # 清除查询项
    #         self.clear(self.seachcustomer)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #
    #         # 输入查询客户的名称
    #         time.sleep(2)
    #         self.input(self.seachcustomer, queryName)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"输入{queryName}输入查询信息",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #         # 点击查询
    #         self.click(self.seach2)
    #         allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach2}点击查询",
    #                       allure.attachment_type.PNG)  # 保存截图为allure的附件
    #         time.sleep(1)
    #         if queryName == "批量模糊查询":
    #             # 获取“批量模糊查询”总条数
    #             time.sleep(1)
    #             self.customerNum = self.obtain_value(self.getcustomerPage)
    #             return self.customerNum
    #         else:
    #             # 获取“客户编码”文本
    #             time.sleep(1)
    #             self.customerNum = self.obtain_value(self.getcustomername)
    #             return self.customerNum
    #     except:
    #         self.refresh()
    #         time.sleep(1)
    #         return "用例失败"

    # 基础资料 删除单条自定义项目信息
    def delete_userdefined(self,deleteName):
        try:
            # self.visit('http://8.142.139.164:8086/?getTokenParams=%7B%22companyNumber%22%3A%22F0013%22%2C%22companyId%22%3A%22b192bc04-9a14-4495-a6d2-f84c55272e8d%22%2C%22userName%22%3A%22%u8D85%u7EA7%u7BA1%u7406%u545822%22%2C%22PSIID%22%3A%2250bdc4cc-9cd3-44f5-b0ca-be5b5f3cc809%22%2C%22Password%22%3A%228ef0fe47-f46b-4d52-9426-02273b8fcff0%22%2C%22departmentId%22%3A%2201940d13-f7d1-4039-b163-344a44c8ec87%22%2C%22jurisdictionid%22%3A10%2C%22isadmin%22%3Atrue%2C%22smallType%22%3A2%2C%22is_machine_accounts%22%3Afalse%2C%22tax_inspection_surpluscount%22%3A0%2C%22tax_number%22%3A0%2C%22uif%22%3A%22Bearer%20eyJhbGciOiJSUzI1NiIsImtpZCI6IjhGRDgyQTlBNDhGODUyMDE3MjAzNTNCRUQ5OUY0NkE1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2NzA4MDkzNzUsImV4cCI6MTY3MDg5NTc3NSwiaXNzIjoiaHR0cDovLzguMTQyLjEzOS4xNjQ6ODkwMC9ZZHpVbmlmeUlkZW50aXR5IiwiYXVkIjoiVW5pZnlBcGkiLCJjbGllbnRfaWQiOiJjbGllbnRfcGMiLCJzdWIiOiI4ZWYwZmU0Ny1mNDZiLTRkNTItOTQyNi0wMjI3M2I4ZmNmZjAiLCJhdXRoX3RpbWUiOjE2NzA4MDkzNzUsImlkcCI6ImxvY2FsIiwiVXNlckluZm8iOiJ7XCJpZFwiOjAsXCJjb21wYW55aWRcIjpcImIxOTJiYzA0LTlhMTQtNDQ5NS1hNmQyLWY4NGM1NTI3MmU4ZFwiLFwiY29tcGFueU5hbWVcIjpudWxsLFwic3ViaWRcIjpcIjNlZTM0YTljLWNjNWEtNGQ3OC1iNGY0LTU4ZTg5MzFjYzc3ZlwiLFwiY29tcGFueW51bWJlclwiOlwiRjAwMTNcIixcImNvbXBhbnlsb2dvXCI6XCJcIixcInVzZXJpZFwiOlwiOGVmMGZlNDctZjQ2Yi00ZDUyLTk0MjYtMDIyNzNiOGZjZmYwXCIsXCJyb2xlaWRcIjpcImNkYTgxMjg3LTRhNjItNGMxOC1iMzgyLTA1ZTU1ZTc0OWM3MlwiLFwiZGVwYXJ0bWVudGlkXCI6XCIwMTk0MGQxMy1mN2QxLTQwMzktYjE2My0zNDRhNDRjOGVjODdcIixcInBob25lXCI6XCIxMzE2MzI1MDYxNVwiLFwidXNlcm5hbWVcIjpcImFkbWluXCIsXCJyZWFsbmFtZVwiOlwi6LaF57qn566h55CG5ZGYMjJcIixcImlzYWRtaW5cIjp0cnVlLFwid29ya051bWJlclwiOm51bGwsXCJzZXJ2aWNlRW5kRGF0ZVwiOlwiMjAyMy0wOC0xMFQwMDowMDowMFwiLFwibG9naW5UeXBlXCI6MCxcImNyZWF0ZVRpbWVcIjpcIjIwMjEtMTItMjRUMTk6NDA6NTFcIixcImNyZWRlbnRpYWxJZFwiOlwiMTAwMDAyMDAzMFwiLFwiYXBwS2V5XCI6XCIxMDAwMjAxMVwiLFwiYXBwU2VjcmV0XCI6XCI1MTA3YWQxZmI1MWNjYTZjZGVmYjZhZDQxNTdiMjU4MGM3YjMzYmNhOTgwYzg5ODBkNDM4OGU0YWU4NzllYTU0MDRiZjM4MzUwXCIsXCJwcm9maWxlXCI6bnVsbCxcInR5cGVcIjowLFwic21hbGxUeXBlXCI6MixcInBvc2l0aW9uXCI6bnVsbCxcImlzQXBwcm92ZVwiOnRydWUsXCJpc1B1cmNoYXNlXCI6dHJ1ZSxcImlzV29ya1wiOnRydWUsXCJpc0J1ZGdldFwiOnRydWUsXCJpc0ludm9pY2VNYW5hZ2VyXCI6dHJ1ZSxcImlzRmluYW5jZVwiOmZhbHNlLFwiaXNIdW1hblJlc291cmNlXCI6ZmFsc2UsXCJpc1RyeVwiOmZhbHNlLFwiaGVhZFBvcnRyYWl0XCI6bnVsbCxcIm5pY2tOYW1lXCI6bnVsbCxcImlzQ2hhbmdlTG9nb1wiOnRydWUsXCJpc0N1c3RvbUxvZ2luXCI6ZmFsc2UsXCJsYXN0TG9naW5Db21wYW55aWRcIjpudWxsLFwiaXNBZ2VudFVzZXJcIjpmYWxzZSxcImFnZW50SWRcIjpudWxsLFwiYWdlbnROYW1lXCI6bnVsbCxcImlzTWFuYWdlclwiOm51bGwsXCJpc1BsYXRmb3JtXCI6bnVsbCxcImlzRmlyc3RMb2dpblwiOm51bGwsXCJ1VmVyc2lvblwiOm51bGwsXCJ1c2VyVHlwZVwiOm51bGwsXCJTeUZpbmFuY2VfbnVtYmVyXCI6OSxcInN0YXR1c1wiOjAsXCJwb3NpdGlvblN0YXR1c1wiOjEsXCJpbmR1c3RyeWlkXCI6MSxcImlzT3BlbldhdGVybWFya1wiOnRydWV9IiwianRpIjoiOUNFOTg4MTZEOTlCMUEwRUEwQzVGQkIzQUI1M0U0MUIiLCJpYXQiOjE2NzA4MDkzNzUsInNjb3BlIjpbIkVwQXBpIiwiR2ZBcGkiLCJOb0NvZGVBcGkiLCJQc2lBcGkiLCJUb3JzaW9uQ2VudGVyQXBpIl0sImFtciI6WyJjdXN0b20iXX0.srL6_5MupTeRgC8aa2cxqQqxuu8ukn4mzZwysjRoISCWu_yxLlHm4vB37-YY0ZXnfI6MXC4XZ6w_8Ny1ZDVeKVv1NESw8vrU1wjJb1KtmQvR0FWKAtQDCQlHuGKzbDQmgWHGk_uPJ46wl-_0BkhXZUGey3unxgESnTgmIGmKJv9cpynHbD8PEyGksWI418c0wzH-1FUTHbXgSyUl9NJoT6WKu8Uhe6JHsZZrsaGAsNnFeugdzyckK9taZRR1uYaDIKrePikadE3oW7l0-PBcX3HREK_dhsaRFhegNtUCgFOXga_SfIsnGfBlE3XHJHeNryO3X3TtEfymB2Fx4oonFA%22%2C%22PSIName%22%3A%22UI%u6D4B%u8BD5%u4E13%u7528%22%2C%22curmoterid%22%3A%2265adf0e4-89ca-4698-b979-6392af69c2c0%22%2C%22companylogo%22%3A%22%22%2C%22isChangeLogo%22%3Atrue%7D&expires=Wed,%2011%20Jan%202023%2001:43:06%20GMT&path=/#/basicSetting/basicData')
            # time.sleep(10)
            self.refresh()
            time.sleep(2)
            # 点击进入自定义项目页面
            link1 = self.driver.find_element(By.ID, 'tab-auxiliaryDatum')
            # 模拟鼠标悬停操作
            action = ActionChains(self.driver)
            action.move_to_element(link1).perform()
            time.sleep(1)
            # 移动鼠标点击UI自动化
            action.move_by_offset(120, 0).click()
            action.perform()


            # 清除查询项
            self.clear(self.seachcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除{self.seachcustomer}清除查询信息",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 输入查询客户的名称
            self.input(self.seachcustomer, "UI自动化新增自定义数据001")
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
    lp = Basic_Setting_userdefined(driver)
    # k = lp.add_Supplier("3231")

    # lp.change_userdefined("名称重复自定义项目")
    # lp.change_userdefined("修改自定义项目数据")
    # lp.add_userdefined("名称重复自定义项目")
    # lp.add_userdefined("UI自动化新增自定义项目人员")
    # lp.seach_userdefined("单个精准查询")
    # lp.seach_userdefined("单个模糊")
    # lp.seach_userdefined("批量模糊查询")
    # lp.delete_userdefined("UI自动化新增自定义项目001")
    lp.delete_userdefined("321")

    driver.quit()