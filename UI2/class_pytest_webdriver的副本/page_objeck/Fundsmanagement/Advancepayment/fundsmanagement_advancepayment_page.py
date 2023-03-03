# coding=UTF-8
"""对象包含：1.预付款单里的增删改查 """
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




class Fund_Management_advancepayment(BasePage):
    # 核心元素
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/fundsmanagement/advance payment/InsertInDatabase.yaml')
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

    # 基础资料 新增预付款单
    def add_advancepayment(self,advancepaymentName):
        try:
        #     self.visit('http://8.142.139.164:8086/?getTokenParams=%7B%22companyNumber%22%3A%22F0013%22%2C%22companyId%22%3A%22b192bc04-9a14-4495-a6d2-f84c55272e8d%22%2C%22userName%22%3A%22%u8D85%u7EA7%u7BA1%u7406%u545822%22%2C%22PSIID%22%3A%2250bdc4cc-9cd3-44f5-b0ca-be5b5f3cc809%22%2C%22Password%22%3A%228ef0fe47-f46b-4d52-9426-02273b8fcff0%22%2C%22departmentId%22%3A%2201940d13-f7d1-4039-b163-344a44c8ec87%22%2C%22jurisdictionid%22%3A10%2C%22isadmin%22%3Atrue%2C%22smallType%22%3A2%2C%22is_machine_accounts%22%3Afalse%2C%22tax_inspection_surpluscount%22%3A0%2C%22tax_number%22%3A0%2C%22uif%22%3A%22Bearer%20eyJhbGciOiJSUzI1NiIsImtpZCI6IjhGRDgyQTlBNDhGODUyMDE3MjAzNTNCRUQ5OUY0NkE1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2NzIxMjM3MjYsImV4cCI6MTY3MjIxMDEyNiwiaXNzIjoiaHR0cDovLzguMTQyLjEzOS4xNjQ6ODkwMC9ZZHpVbmlmeUlkZW50aXR5IiwiYXVkIjoiVW5pZnlBcGkiLCJjbGllbnRfaWQiOiJjbGllbnRfcGMiLCJzdWIiOiI4ZWYwZmU0Ny1mNDZiLTRkNTItOTQyNi0wMjI3M2I4ZmNmZjAiLCJhdXRoX3RpbWUiOjE2NzIxMjM3MjYsImlkcCI6ImxvY2FsIiwiVXNlckluZm8iOiJ7XCJpZFwiOjAsXCJjb21wYW55aWRcIjpcImIxOTJiYzA0LTlhMTQtNDQ5NS1hNmQyLWY4NGM1NTI3MmU4ZFwiLFwiY29tcGFueU5hbWVcIjpudWxsLFwic3ViaWRcIjpcIjNlZTM0YTljLWNjNWEtNGQ3OC1iNGY0LTU4ZTg5MzFjYzc3ZlwiLFwiY29tcGFueW51bWJlclwiOlwiRjAwMTNcIixcImNvbXBhbnlsb2dvXCI6XCJcIixcInVzZXJpZFwiOlwiOGVmMGZlNDctZjQ2Yi00ZDUyLTk0MjYtMDIyNzNiOGZjZmYwXCIsXCJyb2xlaWRcIjpcImNkYTgxMjg3LTRhNjItNGMxOC1iMzgyLTA1ZTU1ZTc0OWM3MlwiLFwiZGVwYXJ0bWVudGlkXCI6XCIwMTk0MGQxMy1mN2QxLTQwMzktYjE2My0zNDRhNDRjOGVjODdcIixcInBob25lXCI6XCIxMzE2MzI1MDYxNVwiLFwidXNlcm5hbWVcIjpcImFkbWluXCIsXCJyZWFsbmFtZVwiOlwi6LaF57qn566h55CG5ZGYMjJcIixcImlzYWRtaW5cIjp0cnVlLFwid29ya051bWJlclwiOm51bGwsXCJzZXJ2aWNlRW5kRGF0ZVwiOlwiMjAyMy0wOC0xMFQwMDowMDowMFwiLFwibG9naW5UeXBlXCI6MCxcImNyZWF0ZVRpbWVcIjpcIjIwMjEtMTItMjRUMTk6NDA6NTFcIixcImNyZWRlbnRpYWxJZFwiOlwiMTAwMDAyMDAzMFwiLFwiYXBwS2V5XCI6XCIxMDAwMjAxMVwiLFwiYXBwU2VjcmV0XCI6XCI0ODk0YWQxZmI1MWNjYTZjZGVmYjZhZDQxNTdiMjU4MGM3YjMzYmNhOTgwYzg5ODBkNDM4OGU0YWU4NzllYTU0MDRiZjUwNTE5XCIsXCJwcm9maWxlXCI6bnVsbCxcInR5cGVcIjowLFwic21hbGxUeXBlXCI6MixcInBvc2l0aW9uXCI6bnVsbCxcImlzQXBwcm92ZVwiOnRydWUsXCJpc1B1cmNoYXNlXCI6dHJ1ZSxcImlzV29ya1wiOnRydWUsXCJpc0J1ZGdldFwiOnRydWUsXCJpc0ludm9pY2VNYW5hZ2VyXCI6dHJ1ZSxcImlzRmluYW5jZVwiOmZhbHNlLFwiaXNIdW1hblJlc291cmNlXCI6ZmFsc2UsXCJpc1RyeVwiOmZhbHNlLFwiaGVhZFBvcnRyYWl0XCI6bnVsbCxcIm5pY2tOYW1lXCI6bnVsbCxcImlzQ2hhbmdlTG9nb1wiOnRydWUsXCJpc0N1c3RvbUxvZ2luXCI6ZmFsc2UsXCJsYXN0TG9naW5Db21wYW55aWRcIjpudWxsLFwiaXNBZ2VudFVzZXJcIjpmYWxzZSxcImFnZW50SWRcIjpudWxsLFwiYWdlbnROYW1lXCI6bnVsbCxcImlzTWFuYWdlclwiOm51bGwsXCJpc1BsYXRmb3JtXCI6bnVsbCxcImlzRmlyc3RMb2dpblwiOm51bGwsXCJ1VmVyc2lvblwiOm51bGwsXCJ1c2VyVHlwZVwiOm51bGwsXCJTeUZpbmFuY2VfbnVtYmVyXCI6OSxcInN0YXR1c1wiOjAsXCJwb3NpdGlvblN0YXR1c1wiOjEsXCJpbmR1c3RyeWlkXCI6MSxcImlzT3BlbldhdGVybWFya1wiOnRydWV9IiwianRpIjoiODIyNzhGOTZBQzQzMDREOUY2RTdEMjJCQjYyNzk5MDAiLCJpYXQiOjE2NzIxMjM3MjYsInNjb3BlIjpbIkVwQXBpIiwiR2ZBcGkiLCJOb0NvZGVBcGkiLCJQc2lBcGkiLCJUb3JzaW9uQ2VudGVyQXBpIl0sImFtciI6WyJjdXN0b20iXX0.bCIPeQR7OoC4-0OdsuajgzR374msXzQb7MDRD0OANZJi_sJcDyNWJyIhEQAfu-efihEzZxnamVbLUPlrunFWlf6ESwDyKAy_xyzFHpUoloH06dIRX-9qvPiOLKCqDiub4sLBGgkDbS3flA4o2eVkOuJhx7IKpmL1XfBs5z9cj9B7eWbBNK0PAe4eEQMor1Sbpi838XL7_Qgg7pTawLVon32AEgkjllgx7mNWrdYbljNzWXYjWmIyrxCx_zJF0iT_byZDB9wvSUyBf7WvsvfEQc8EtBT6Kp5TrMQefTD1-ULlHphNqzVc_JL3mAEEdxVv-mZ0J1gY1aYmqIby0E9a1Q%22%2C%22PSIName%22%3A%22UI%u6D4B%u8BD5%u4E13%u7528%22%2C%22curmoterid%22%3A%2265adf0e4-89ca-4698-b979-6392af69c2c0%22%2C%22companylogo%22%3A%22%22%2C%22isChangeLogo%22%3Atrue%7D&expires=Thu,%2026%20Jan%202023%2006:50:41%20GMT&path=/#/bills/advancePayment')
        #     time.sleep(10)

            if advancepaymentName == "UI自动化新增预付款单003":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.customer,'')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 点击输入日期
                self.clear(self.date)
                allure.attach(self.driver.get_screenshot_as_png(), f"清空日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.date,"2022-12-01")
                allure.attach(self.driver.get_screenshot_as_png(), f"输入日期",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                self.input(self.account, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入账户",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件
                time.sleep(2)

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advancePayment"]/div[2]/div[4]/div/div/input')
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

                # 获取提示弹窗文本
                self.a = self.driver.find_element_by_class_name('el-message__content').text
                return self.a

            elif advancepaymentName == "UI自动化新增预付款单001":
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.customer,'单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH,'//*[@id="advancePayment"]/div[2]/div[2]/div/div/input')
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advancePayment"]/div[2]/div[4]/div/div/input')
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

                self.input(self.money,"1000")
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

            elif advancepaymentName == "UI自动化新增预付款单002":
                self.click(self.resh)
                time.sleep(2)
                # # 点击输入供应商名称
                self.input(self.customer, '单个精准查询')
                allure.attach(self.driver.get_screenshot_as_png(), f"点击输入供应商名称",
                              allure.attachment_type.PNG)  # 保存截图为allure的附件

                # 模拟鼠标悬停操作
                action = ActionChains(self.driver)
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advancePayment"]/div[2]/div[2]/div/div/input')
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
                link1 = self.driver.find_element(By.XPATH, '//*[@id="advancePayment"]/div[2]/div[4]/div/div/input')
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
    def change_advancepayment(self,changeCustomerName):
        try:

            self.click(self.resh)
            time.sleep(2)
                # 点击末张
            self.click(self.last)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击末张",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件

            if changeCustomerName == '修改预付款单数据01':
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


    # 基础资料 删除单条供应商信息
    def delete_advancepayment(self,deleteName):
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
    lp = Fund_Management_advancepayment(driver)
    k = lp.add_advancepayment("UI自动化新增预付款单001")
    # lp.seach_advancepayment("单个精准查询")
    # lp.delete_advancepayment("UI自动化新增预付款单001")
    # lp.change_advancepayment("修改预付款单数据02")

    driver.quit()