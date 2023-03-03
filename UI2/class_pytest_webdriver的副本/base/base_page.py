"""base_page 基类提供常用函数"""
import time
from time import sleep
from typing import Tuple

import allure
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


Locator = Tuple[By, str]



class BasePage:
    def __init__(self, init_driver):
        self.driver = init_driver
        self.seconds = 10

    # 访问url
    def visit(self,url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return WebDriverWait(self.driver, self.seconds, 1).until(
            EC.presence_of_element_located(loc))
        # return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    # 清除
    def clear(self,loc):
        self.locator(loc).clear()
    #
    # 悬浮
    def move(self,loc):
        self.driver.move_to(loc)

    # 点击
    def click(self, loc):
        self.locator(loc).click()
        sleep(2)

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 获取当前页面url
    def obtain_url(self):
        sleep(1)
        # WebDriverWait(self.driver, 10, 1).until(self.driver.current_url())

        return self.driver.current_url

    # 获取元素的值
    def obtain_value(self,loc):
        # return WebDriverWait(self.driver, 10, 1).until(self.locator(loc).text)
        return self.locator(loc).text

    # 进入frame框架
    def goto_frame(self,frame_name):
        # sleep(1)
        self.driver.switch_to_frame(frame_name)

    # 退出frame框架
    def quit_frame(self):
        # sleep(1)
        self.driver.switch_to_default_content()

    # 下拉框选择
    def choixce_select(self,loc,value):
        sel = Select(self.locator(loc))
        sel.select_by_value(value)



    # 刷新当前页面
    def refresh(self):
        self.driver.refresh()
