from selenium import webdriver
import time
from data.url import *
class Setup:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
