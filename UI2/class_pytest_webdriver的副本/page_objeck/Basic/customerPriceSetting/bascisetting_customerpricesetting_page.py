# coding=UTF-8
"""基础设置对象包含：1.基础资料里客户价格设置的增删改查 """
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver
from base.login import Login




class Basic_Setting_customerpricesetting(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/customerPriceSetting/invertonyDatabase.yaml')
    data1 = data[0]['BasicSetting']
    # 新增按钮
    addnewcustomer =(By.XPATH, data1['addnewcustomer'])
    #   新增名称输入位置
    newcustomername=(By.XPATH, data1['newcustomername'])
    #   选择价格类型
    pricetype=(By.XPATH, data1['pricetype'])
    #   展开下拉框选择 客户+存货
    pricetype1=(By.XPATH, data1['pricetype1'])
    #   输入开始时间
    startime=(By.XPATH, data1['startime'])
    #   输入结束时间
    endtime=(By.XPATH, data1['endtime'])
    #   下一步
    next=(By.XPATH, data1['next'])
    #   配置客户页面-添加
    addcustomer=(By.XPATH, data1['addcustomer'])
    #   勾选框
    chick=(By.XPATH, data1['chick'])
    #   确定按钮
    dochick=(By.XPATH, data1['dochick'])
    #   下一步
    next1=(By.XPATH, data1['next1'])
    #   配置存货页面- 添加
    addinventory=(By.XPATH, data1['addinventory'])
    #   失败勾选框
    chick1=(By.XPATH, data1['chick1'])
    #   成功勾选框
    chick2=(By.XPATH, data1['chick2'])
    # 确定按钮
    dochick2=(By.XPATH, data1['dochick2'])
    #  下一步
    next2=(By.XPATH, data1['next2'])

    update=(By.XPATH, data1['update'])

    #   删除客户
    delcus=(By.XPATH, data1['delcus'])
    #   删除存货
    delinven=(By.XPATH, data1['delinven'])

    #   删除按钮
    delete=(By.XPATH, data1['delete'])
    #   确认删除
    dodelete=(By.XPATH, data1['dodelete'])
    # "共0条"
    NULL1=(By.XPATH, data1['NULL1'])
    # 输入名称查询位置
    seach=(By.XPATH, data1['seach'])
    #   查询
    doseach=(By.XPATH, data1['doseach'])
    # 刷新当前页面
    resh=(By.XPATH, data1['doseach'])
    # 基础资料 新增客户价格设置
    def add_customerpricesetting(self,customerpricesettingName):
        try:
            self.refresh()
            time.sleep(3)
            # 点击新增
            self.click(self.addnewcustomer)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.addnewcustomer}点击新增",allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 第一个页面
            # 输入名称
            self.input(self.newcustomername, customerpricesettingName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入名称",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.pricetype)
            allure.attach(self.driver.get_screenshot_as_png(), f"展开下拉框",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.pricetype1)
            allure.attach(self.driver.get_screenshot_as_png(), f"选择类型",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.input(self.startime, "2022-12-11")
            self.input(self.endtime, "2022-12-11")
            allure.attach(self.driver.get_screenshot_as_png(), f"输入时间",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.next)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 第二个页面
            if customerpricesettingName == "UI自动化新增客户价格设置004":
                self.click(self.next1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.addcustomer)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击添加",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.click(self.chick)
                allure.attach(self.driver.get_screenshot_as_png(), f"选择客户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.click(self.dochick)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击确定",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                self.click(self.next1)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

            # 第三个页面
            if customerpricesettingName == "UI自动化新增客户价格设置003":
                self.click(self.next2)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            else:
                self.click(self.addinventory)
                allure.attach(self.driver.get_screenshot_as_png(), f"点击新增",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                if customerpricesettingName == "UI自动化新增客户价格设置001":
                    self.click(self.chick2)
                    allure.attach(self.driver.get_screenshot_as_png(), f"选择存货",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    self.click(self.dochick2)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击确定",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                else:
                    self.click(self.chick1)
                    allure.attach(self.driver.get_screenshot_as_png(), f"选择存货",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
                    self.click(self.dochick2)
                    allure.attach(self.driver.get_screenshot_as_png(), f"点击确定",
                                  allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击下一步
            self.click(self.next2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件


            self.a = self.driver.find_element_by_class_name('el-message').text

            return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(3)
            return "用例执行失败"

    # 基础资料 修改客户价格设置信息
    def change_customerpricesetting(self,updatename):
        try:
            # self.visit('http://8.142.139.164:8086/?getTokenParams=%7B%22companyNumber%22%3A%22F0013%22%2C%22companyId%22%3A%22b192bc04-9a14-4495-a6d2-f84c55272e8d%22%2C%22userName%22%3A%22%u8D85%u7EA7%u7BA1%u7406%u545822%22%2C%22PSIID%22%3A%2250bdc4cc-9cd3-44f5-b0ca-be5b5f3cc809%22%2C%22Password%22%3A%228ef0fe47-f46b-4d52-9426-02273b8fcff0%22%2C%22departmentId%22%3A%2201940d13-f7d1-4039-b163-344a44c8ec87%22%2C%22jurisdictionid%22%3A10%2C%22isadmin%22%3Atrue%2C%22smallType%22%3A2%2C%22is_machine_accounts%22%3Afalse%2C%22tax_inspection_surpluscount%22%3A0%2C%22tax_number%22%3A0%2C%22uif%22%3A%22Bearer%20eyJhbGciOiJSUzI1NiIsImtpZCI6IjhGRDgyQTlBNDhGODUyMDE3MjAzNTNCRUQ5OUY0NkE1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2NzA5OTgxMTksImV4cCI6MTY3MTA4NDUxOSwiaXNzIjoiaHR0cDovLzguMTQyLjEzOS4xNjQ6ODkwMC9ZZHpVbmlmeUlkZW50aXR5IiwiYXVkIjoiVW5pZnlBcGkiLCJjbGllbnRfaWQiOiJjbGllbnRfcGMiLCJzdWIiOiI4ZWYwZmU0Ny1mNDZiLTRkNTItOTQyNi0wMjI3M2I4ZmNmZjAiLCJhdXRoX3RpbWUiOjE2NzA5OTgxMTksImlkcCI6ImxvY2FsIiwiVXNlckluZm8iOiJ7XCJpZFwiOjAsXCJjb21wYW55aWRcIjpcImIxOTJiYzA0LTlhMTQtNDQ5NS1hNmQyLWY4NGM1NTI3MmU4ZFwiLFwiY29tcGFueU5hbWVcIjpudWxsLFwic3ViaWRcIjpcIjNlZTM0YTljLWNjNWEtNGQ3OC1iNGY0LTU4ZTg5MzFjYzc3ZlwiLFwiY29tcGFueW51bWJlclwiOlwiRjAwMTNcIixcImNvbXBhbnlsb2dvXCI6XCJcIixcInVzZXJpZFwiOlwiOGVmMGZlNDctZjQ2Yi00ZDUyLTk0MjYtMDIyNzNiOGZjZmYwXCIsXCJyb2xlaWRcIjpcImNkYTgxMjg3LTRhNjItNGMxOC1iMzgyLTA1ZTU1ZTc0OWM3MlwiLFwiZGVwYXJ0bWVudGlkXCI6XCIwMTk0MGQxMy1mN2QxLTQwMzktYjE2My0zNDRhNDRjOGVjODdcIixcInBob25lXCI6XCIxMzE2MzI1MDYxNVwiLFwidXNlcm5hbWVcIjpcImFkbWluXCIsXCJyZWFsbmFtZVwiOlwi6LaF57qn566h55CG5ZGYMjJcIixcImlzYWRtaW5cIjp0cnVlLFwid29ya051bWJlclwiOm51bGwsXCJzZXJ2aWNlRW5kRGF0ZVwiOlwiMjAyMy0wOC0xMFQwMDowMDowMFwiLFwibG9naW5UeXBlXCI6MCxcImNyZWF0ZVRpbWVcIjpcIjIwMjEtMTItMjRUMTk6NDA6NTFcIixcImNyZWRlbnRpYWxJZFwiOlwiMTAwMDAyMDAzMFwiLFwiYXBwS2V5XCI6XCIxMDAwMjAxMVwiLFwiYXBwU2VjcmV0XCI6XCI1NDQzYWQxZmI1MWNjYTZjZGVmYjZhZDQxNTdiMjU4MGM3YjMzYmNhOTgwYzg5ODBkNDM4OGU0YWU4NzllYTU0MDRiZjA1OTgzXCIsXCJwcm9maWxlXCI6bnVsbCxcInR5cGVcIjowLFwic21hbGxUeXBlXCI6MixcInBvc2l0aW9uXCI6bnVsbCxcImlzQXBwcm92ZVwiOnRydWUsXCJpc1B1cmNoYXNlXCI6dHJ1ZSxcImlzV29ya1wiOnRydWUsXCJpc0J1ZGdldFwiOnRydWUsXCJpc0ludm9pY2VNYW5hZ2VyXCI6dHJ1ZSxcImlzRmluYW5jZVwiOmZhbHNlLFwiaXNIdW1hblJlc291cmNlXCI6ZmFsc2UsXCJpc1RyeVwiOmZhbHNlLFwiaGVhZFBvcnRyYWl0XCI6bnVsbCxcIm5pY2tOYW1lXCI6bnVsbCxcImlzQ2hhbmdlTG9nb1wiOnRydWUsXCJpc0N1c3RvbUxvZ2luXCI6ZmFsc2UsXCJsYXN0TG9naW5Db21wYW55aWRcIjpudWxsLFwiaXNBZ2VudFVzZXJcIjpmYWxzZSxcImFnZW50SWRcIjpudWxsLFwiYWdlbnROYW1lXCI6bnVsbCxcImlzTWFuYWdlclwiOm51bGwsXCJpc1BsYXRmb3JtXCI6bnVsbCxcImlzRmlyc3RMb2dpblwiOm51bGwsXCJ1VmVyc2lvblwiOm51bGwsXCJ1c2VyVHlwZVwiOm51bGwsXCJTeUZpbmFuY2VfbnVtYmVyXCI6OSxcInN0YXR1c1wiOjAsXCJwb3NpdGlvblN0YXR1c1wiOjEsXCJpbmR1c3RyeWlkXCI6MSxcImlzT3BlbldhdGVybWFya1wiOnRydWV9IiwianRpIjoiOTMxM0I1NTM4QzU5MUFGQkQ0NUNERjY5N0EzODE5Q0UiLCJpYXQiOjE2NzA5OTgxMTksInNjb3BlIjpbIkVwQXBpIiwiR2ZBcGkiLCJOb0NvZGVBcGkiLCJQc2lBcGkiLCJUb3JzaW9uQ2VudGVyQXBpIl0sImFtciI6WyJjdXN0b20iXX0.xBqE48Rf-JW8chDVtZnEcTlmY-uBdJfSaP8_d1sN426fVhpHJa6YQcBdMDy21QCieqwQGpW7w0vu_yhyLLlRkRMaX3135oATERls1LtmYAgjiGK1t8RIK4JNlYvY8rAM7dNHjZezoFA0NlDtjIdikmkuwBweHIAc7D9Jxbi9ovuqaC00lHpqEGHd0alspB-EZ4j48IAxXvAHW9f8I8CQ_Ng_5zLnTurAGlMx9JiHFyzsz1_xmfFuzANksiHhf0SOlG5h_g5mqmMwicCKm1cg_5LD6cE12WaF6lukp7jJb1w8TcENbiL_iLkaH7wSe5GB2zzWgI-S3d_9sJV6o8NG7w%22%2C%22PSIName%22%3A%22UI%u6D4B%u8BD5%u4E13%u7528%22%2C%22curmoterid%22%3A%2265adf0e4-89ca-4698-b979-6392af69c2c0%22%2C%22companylogo%22%3A%22%22%2C%22isChangeLogo%22%3Atrue%7D&expires=Fri,%2013%20Jan%202023%2006:08:46%20GMT&path=/#/basicSetting/clientPriceSetting')
            self.refresh()
            time.sleep(10)
            # 点击修改按钮
            self.click(self.update)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击修改按钮",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 清除开始时间和结束时间
            self.clear(self.startime)
            self.clear(self.endtime)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除开始时间和结束时间",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 重新输入开始时间和结束时间
            self.input(self.startime,updatename)
            self.input(self.endtime,updatename)
            allure.attach(self.driver.get_screenshot_as_png(), f"重新输入开始时间和结束时间",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击下一步
            self.click(self.next)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(1)
            if updatename == "客户为空":
                self.click(self.delcus)
                allure.attach(self.driver.get_screenshot_as_png(), f"删除客户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击下一步
            self.click(self.next1)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            if updatename == "存货为空":
                self.click(self.delinven)
                allure.attach(self.driver.get_screenshot_as_png(), f"删除存货",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击下一步
            self.click(self.next2)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击下一步",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 获取提示弹窗文本
            self.a = self.driver.find_element_by_class_name('el-message').text
            return self.a

        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(2)
            return "用例执行失败"

    # 基础资料 删除单条客户价格设置信息
    def delete_customerpricesetting(self,deleteName):
        try:
            self.refresh()
            time.sleep(3)
            self.clear(self.seach)
            allure.attach(self.driver.get_screenshot_as_png(), f"清除查询项",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.input(self.seach,deleteName)
            allure.attach(self.driver.get_screenshot_as_png(), f"输入查询内容",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.doseach)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击搜索",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.delete)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击删除",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.dodelete)
            allure.attach(self.driver.get_screenshot_as_png(), f"确认删除",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            self.click(self.resh)
            time.sleep(3)
            self.a = self.obtain_value(self.NULL1)
            return self.a
        except:
            allure.attach(self.driver.get_screenshot_as_png(), f"失败截图",

                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.refresh()
            time.sleep(2)
            return "用例执行失败"



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Basic_Setting_customerpricesetting(driver)
    # lp.change_customerpricesetting("存货为空")
    # lp.change_customerpricesetting("修改客户价格设置数据")
    # lp.add_customerpricesetting("名称重复客户价格设置")
    # lp.add_customerpricesetting("UI自动化新增客户价格设置004")
    # lp.seach_customerpricesetting("单个精准查询")
    # lp.seach_customerpricesetting("单个模糊")
    # lp.seach_customerpricesetting("批量模糊查询")
    # lp.delete_customerpricesetting("UI自动化新增客户价格设置001")
    # lp.delete_customerpricesetting("32131")
    driver.quit()