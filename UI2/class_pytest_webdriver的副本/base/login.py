import pytest

from data.url import *
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.yamlload import loadyaml
import allure
from selenium import webdriver

from selenium import webdriver
import time
import json



class Login(BasePage):
    data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/login/ysdw.yaml')
    data1 = data[0]['login']
    navContent = (By.XPATH,data1['navContent'])
    seach = (By.XPATH,data1['seach'])
    seach1 = (By.XPATH, data1['seach1'])
    openSelltext = (By.XPATH,data1['openSelltext'])

    # 测试环境
    def login1(self):
        driver = self.driver
        self.visit(base_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        try:
            driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[1]/div[2]/span[1]').click()
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[1]/div/div/input').send_keys('f0013')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[2]/div/div/input').send_keys('admin')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[3]/div/div/input').send_keys('Ydz123...')
            driver.find_element_by_xpath('//*[@id="login-account"]/div[2]/button/span').click()
            # 点击企业管理
            time.sleep(2)
            self.click(self.navContent)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}选择企业后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            time.sleep(3)
            # 查询固定的账套点击进入
            self.input(self.seach, 'ui')
            # time.sleep(3)
            self.click(self.seach1)
            # self.click(self.seach1)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}进入账套后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 打开进销存
            self.click(self.openSelltext)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.openSelltext}打开进销存后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 切换窗口
            self.driver.switch_to.window(self.driver.window_handles[1])

            # # 获取当前url
            # global homeIndex
            # homeIndex = self.driver.current_url
            return self.driver.current_url
        except:
            self.refresh()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[1]/div[2]/span[1]').click()
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[1]/div/div/input').send_keys('f0013')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[2]/div/div/input').send_keys('admin')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[3]/div/div/input').send_keys('Ydz123...')
            driver.find_element_by_xpath('//*[@id="login-account"]/div[2]/button/span').click()

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
            self.driver.switch_to.window(self.driver.window_handles[1])
            # time.sleep(2)
            return self.driver.current_url


    # 正式环境
    def login2(self):
        driver = self.driver
        self.visit(base_url1)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        try:

            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[1]/div/div/input').send_keys('f0011')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[2]/div/div/input').send_keys('admin')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[3]/div/div/input').send_keys('Ydz123...')
            driver.find_element_by_xpath('//*[@id="login-account"]/div[2]/button/span').click()

            # 查询固定的账套点击进入
            self.input(self.seach, 'ui')
            time.sleep(2)
            self.click(self.seach1)
            self.click(self.seach1)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}进入账套后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件


            # 打开进销存
            self.click(self.openSelltext)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.openSelltext}打开进销存后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 切换窗口
            self.driver.switch_to.window(self.driver.window_handles[1])

            #  获取当前url
            return self.driver.current_url
        except:
            self.refresh()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[1]/div/div/input').send_keys('f0011')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[2]/div/div/input').send_keys('admin')
            driver.find_element_by_xpath('//*[@id="login-account"]/form/div[3]/div/div/input').send_keys('Ydz123...')
            driver.find_element_by_xpath('//*[@id="login-account"]/div[2]/button/span').click()

            # 查询固定的账套点击进入
            self.input(self.seach, 'ui')
            time.sleep(2)
            self.click(self.seach1)
            self.click(self.seach1)
            allure.attach(self.driver.get_screenshot_as_png(), f"点击{self.seach1}进入账套后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 打开进销存
            self.click(self.openSelltext)
            allure.attach(self.driver.get_screenshot_as_png(), f"对{self.openSelltext}打开进销存后",
                          allure.attachment_type.PNG)  # 保存截图为allure的附件
            # 切换窗口
            self.driver.switch_to.window(self.driver.window_handles[1])
            # time.sleep(2)
            return self.driver.current_url




if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = Login(driver)
    a.login2()

