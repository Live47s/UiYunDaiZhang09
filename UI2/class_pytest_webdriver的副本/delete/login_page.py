# coding=UTF-8
"""登录页面对象包含：1核心页面元素：账号，密码，登录按钮等 2.核心业务流程：用户登录行为"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver
import time

class LgoinPage(BasePage):
    # 核心元素
    data = loadyaml('/ysdw.yaml')
    data1 = data[0]['login']
    url = data1['url']
    loginbow = (By.XPATH, data1['loginbow'])
    company = (By.XPATH,data1['company'])
    uesr = (By.XPATH,data1['ustext'])
    pwd = (By.XPATH,data1['pwdtext'])
    login_btn = (By.XPATH,data1['lgbttext'])
    navContent = (By.XPATH,data1['navContent'])
    seach = (By.XPATH,data1['seach'])
    seach1 = (By.XPATH, data1['seach1'])
    openSelltext = (By.XPATH,data1['openSelltext'])


 # 核心业务流
    def login(self,company,username,pwd):
        try:
            self.visit(self.url)
            allure.attach(self.url,"访问网址的网址", allure.attachment_type.TEXT)  # 保存文本为allure的附件
            self.driver.maximize_window()
            self.click(self.loginbow)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.loginbow}登录后",allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.input(self.company, company)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.company}输入的账号{company}后",allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.input(self.uesr,username)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.uesr}输入的账号{username}后", allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.input(self.pwd,pwd)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.pwd}输入的密码{pwd}后",allure.attachment_type.PNG)  # 保存截图为allure的附件
            self.click(self.login_btn)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.login_btn}登录后",allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 点击企业管理
            time.sleep(2)
            self.click(self.navContent)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}选择企业后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 查询固定的账套点击进入
            self.input(self.seach, 'ui')
            time.sleep(3)
            self.click(self.seach1)
            self.click(self.seach1)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}进入账套后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 打开进销存
            self.click(self.openSelltext)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.openSelltext}打开进销存后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 切换窗口
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            # 获取当前url
            global homeIndex
            homeIndex = self.driver.current_url
            return homeIndex

        except:
            return self.driver.current_url



if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LgoinPage(driver)
    lp.login("f0013","admin","Ydz123...")
    driver.quit()