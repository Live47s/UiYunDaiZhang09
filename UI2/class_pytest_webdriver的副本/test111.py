# coding=utf-8
import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("http://enterprise.91yikuaiji.com:8756/")
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/div[1]/div[1]/ul/div[2]/li/div/span').click
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/div[1]/div[1]/ul/div[2]/li/ul/li/ul/li[1]/span').click
# from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

#

# driver.get('http://enterprise.91yikuaiji.com:8756')
# driver.find_element(By.XPATH,'//*[@id="login"]/div[2]/div[1]/div[2]/span[1]').click()
# company = 'f0013'
# userename = 'admin'
# pwd = 'Ydz123...'
# # lp = LgoinPage(driver)
# # lo = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[1]/div[2]/span[1]')
# # lo.click()
# # a = lp.login('http://enterprise.91yikuaiji.com:8756', company, userename, pwd)
# time.sleep(5)
# c = driver.find_element(By.XPATH,'//*[@id="cancelAccountContainer"]/div[2]/div[1]/div[1]/ul/li[3]/button/span/span')
# c.click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[1])
# # d =driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[1]/div[1]/ul/div[2]/li/div/span')
# # d.click()
# time.sleep(3)
#
# 点击新增
driver = webdriver.Chrome()
driver.maximize_window()
# a = Login(driver)
# a.login1()
# time.sleep(3)
# # 鼠标悬浮到基础设置按钮
# link1 = driver.find_element(By.XPATH,
#                                  '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
# # 模拟鼠标悬停操作
# action = ActionChains(driver)
# action.move_to_element(link1).perform()
# time.sleep(2)
# # 移动鼠标点击基础资料
# action.move_by_offset(100, 40).click()
# action.perform()
#
driver.get('http://8.142.139.164:8086/?getTokenParams=%7B%22companyNumber%22%3A%22F0013%22%2C%22companyId%22%3A%22b192bc04-9a14-4495-a6d2-f84c55272e8d%22%2C%22userName%22%3A%22%u8D85%u7EA7%u7BA1%u7406%u545822%22%2C%22PSIID%22%3A%2250bdc4cc-9cd3-44f5-b0ca-be5b5f3cc809%22%2C%22Password%22%3A%228ef0fe47-f46b-4d52-9426-02273b8fcff0%22%2C%22departmentId%22%3A%2201940d13-f7d1-4039-b163-344a44c8ec87%22%2C%22jurisdictionid%22%3A10%2C%22isadmin%22%3Atrue%2C%22smallType%22%3A2%2C%22is_machine_accounts%22%3Afalse%2C%22tax_inspection_surpluscount%22%3A0%2C%22tax_number%22%3A0%2C%22uif%22%3A%22Bearer%20eyJhbGciOiJSUzI1NiIsImtpZCI6IjhGRDgyQTlBNDhGODUyMDE3MjAzNTNCRUQ5OUY0NkE1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2NzA0OTUxNDcsImV4cCI6MTY3MDU4MTU0NywiaXNzIjoiaHR0cDovLzguMTQyLjEzOS4xNjQ6ODkwMC9ZZHpVbmlmeUlkZW50aXR5IiwiYXVkIjoiVW5pZnlBcGkiLCJjbGllbnRfaWQiOiJjbGllbnRfcGMiLCJzdWIiOiI4ZWYwZmU0Ny1mNDZiLTRkNTItOTQyNi0wMjI3M2I4ZmNmZjAiLCJhdXRoX3RpbWUiOjE2NzA0OTUxNDcsImlkcCI6ImxvY2FsIiwiVXNlckluZm8iOiJ7XCJpZFwiOjAsXCJjb21wYW55aWRcIjpcImIxOTJiYzA0LTlhMTQtNDQ5NS1hNmQyLWY4NGM1NTI3MmU4ZFwiLFwiY29tcGFueU5hbWVcIjpudWxsLFwic3ViaWRcIjpcIjNlZTM0YTljLWNjNWEtNGQ3OC1iNGY0LTU4ZTg5MzFjYzc3ZlwiLFwiY29tcGFueW51bWJlclwiOlwiRjAwMTNcIixcImNvbXBhbnlsb2dvXCI6XCJcIixcInVzZXJpZFwiOlwiOGVmMGZlNDctZjQ2Yi00ZDUyLTk0MjYtMDIyNzNiOGZjZmYwXCIsXCJyb2xlaWRcIjpcImNkYTgxMjg3LTRhNjItNGMxOC1iMzgyLTA1ZTU1ZTc0OWM3MlwiLFwiZGVwYXJ0bWVudGlkXCI6XCIwMTk0MGQxMy1mN2QxLTQwMzktYjE2My0zNDRhNDRjOGVjODdcIixcInBob25lXCI6XCIxMzE2MzI1MDYxNVwiLFwidXNlcm5hbWVcIjpcImFkbWluXCIsXCJyZWFsbmFtZVwiOlwi6LaF57qn566h55CG5ZGYMjJcIixcImlzYWRtaW5cIjp0cnVlLFwid29ya051bWJlclwiOm51bGwsXCJzZXJ2aWNlRW5kRGF0ZVwiOlwiMjAyMy0wOC0xMFQwMDowMDowMFwiLFwibG9naW5UeXBlXCI6MCxcImNyZWF0ZVRpbWVcIjpcIjIwMjEtMTItMjRUMTk6NDA6NTFcIixcImNyZWRlbnRpYWxJZFwiOlwiMTAwMDAyMDAzMFwiLFwiYXBwS2V5XCI6XCIxMDAwMjAxMVwiLFwiYXBwU2VjcmV0XCI6XCIwMjAyYWQxZmI1MWNjYTZjZGVmYjZhZDQxNTdiMjU4MGM3YjMzYmNhOTgwYzg5ODBkNDM4OGU0YWU4NzllYTU0MDRiZjM0MTI3XCIsXCJwcm9maWxlXCI6bnVsbCxcInR5cGVcIjowLFwic21hbGxUeXBlXCI6MixcInBvc2l0aW9uXCI6bnVsbCxcImlzQXBwcm92ZVwiOnRydWUsXCJpc1B1cmNoYXNlXCI6dHJ1ZSxcImlzV29ya1wiOnRydWUsXCJpc0J1ZGdldFwiOnRydWUsXCJpc0ludm9pY2VNYW5hZ2VyXCI6dHJ1ZSxcImlzRmluYW5jZVwiOmZhbHNlLFwiaXNIdW1hblJlc291cmNlXCI6ZmFsc2UsXCJpc1RyeVwiOmZhbHNlLFwiaGVhZFBvcnRyYWl0XCI6bnVsbCxcIm5pY2tOYW1lXCI6bnVsbCxcImlzQ2hhbmdlTG9nb1wiOnRydWUsXCJpc0N1c3RvbUxvZ2luXCI6ZmFsc2UsXCJsYXN0TG9naW5Db21wYW55aWRcIjpudWxsLFwiaXNBZ2VudFVzZXJcIjpmYWxzZSxcImFnZW50SWRcIjpudWxsLFwiYWdlbnROYW1lXCI6bnVsbCxcImlzTWFuYWdlclwiOm51bGwsXCJpc1BsYXRmb3JtXCI6bnVsbCxcImlzRmlyc3RMb2dpblwiOm51bGwsXCJ1VmVyc2lvblwiOm51bGwsXCJ1c2VyVHlwZVwiOm51bGwsXCJTeUZpbmFuY2VfbnVtYmVyXCI6OSxcInN0YXR1c1wiOjAsXCJwb3NpdGlvblN0YXR1c1wiOjEsXCJpbmR1c3RyeWlkXCI6MSxcImlzT3BlbldhdGVybWFya1wiOnRydWV9IiwianRpIjoiRkMxOTQ3NDQ3MTk5MTlDQjM4NjJDQzg2QjhCNzk1QUMiLCJpYXQiOjE2NzA0OTUxNDcsInNjb3BlIjpbIkVwQXBpIiwiR2ZBcGkiLCJOb0NvZGVBcGkiLCJQc2lBcGkiLCJUb3JzaW9uQ2VudGVyQXBpIl0sImFtciI6WyJjdXN0b20iXX0.siTgIYQV3KCnf4kicaJL-3RVYCfdFp0ZJxY1tqC-7VZ9dhqUlVf0zdblZUKWuWwbG782Scksd7zKbxTwsEaGmXzBYpIsoBemyaLYN-ZSv5D3BfV-H6UltBuDiIZndg9fogZGM0P1hJ7Z_fz2TojbnMG-sVxlI2RBm3hG2OPh_R-ZeS3F8j7tpMz_fGxF70OgM-wN8ABc5-LoHuhjWybWgwi7bCjwEH_UgGFN3kVqhJibQe0xAagBEI7y15PHbDzHe1Sb4u9W3gw40uIDDrhmsccremJx8GefOrmJRck9Bfh75Ho-C5Ce_JtMg_ULoL1jYfa9LTLCkdJ5wbrqtQDxxQ%22%2C%22PSIName%22%3A%22UI%u6D4B%u8BD5%u4E13%u7528%22%2C%22curmoterid%22%3A%2265adf0e4-89ca-4698-b979-6392af69c2c0%22%2C%22companylogo%22%3A%22%22%2C%22isChangeLogo%22%3Atrue%7D&expires=Sat,%2007%20Jan%202023%2010:26:00%20GMT&path=/#/basicSetting/basicData')
time.sleep(6)
# driver.find_element(By.CLASS_NAME, 'Addplus').click()
# # 输入名称
# driver.find_element(By.XPATH, '//*[@id="Newcategory"]/div/div/div[2]/div/div/input').send_keys('UI自动化')
# # 点击确定
# driver.find_element(By.XPATH, '//*[@id="Newcategory"]/div/div/div[3]/span/button[2]/span').click()
# 鼠标悬浮到基础辅助资料按钮
driver.implicitly_wait(10)
# time.sleep(3)
# link2 = driver.find_element(By.CLASS_NAME,'el-tabs__item is-top')
link2 = driver.find_element(By.XPATH,'//*[@id="tab-AuxiliaryAttributes"]/../div[12]/span/span/span/span').click()
driver.find_element(By.XPATH,'//*[@class="el-popover el-popper popoverStyle"]/../div/span[2]').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/button[2]/span').click()
# link2.click()
time.sleep(3)
# 模拟鼠标悬停操作
# action = ActionChains(driver)
# action.move_to_element(link2).perform()
# time.sleep(3)
# # # 移动鼠标
# action.move_by_offset(120, 0).click()
# time.sleep(3)
# action.perform()
# # 找到需要悬停的页面元素
# link1 =driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/div[1]/ul/li[2]/span/span/div/div/div/span')
# # 模拟鼠标悬停操作
# action = ActionChains(driver)
# action.move_to_element(link1).perform()
# time.sleep(2)
# # 移动鼠标
# action.move_by_offset(100,40).click()
# action.perform()
# time.sleep(5)
#
# # 滑动横向滚动条
# js = 'document.getElementsByClassName("elx-table--footer-wrapper body--wrapper")[0].scrollLeft=10000'
# driver.execute_script(js)
# time.sleep(5)

# e =driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[1]/div[1]/ul/div[2]/li/ul/li/ul/li[1]/span')
# e.click()

# driver.close()

#purchaseorder > div.pageMain > div > div.singleTable.elx-grid.t--animat > div > div.elx-table--main-wrapper > div.elx-table--footer-wrapper.body--wrapper > table
# a = random.randint(1,1000)
# print(a)
#
# data = loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/basic/InsertInDatabase.yaml')
# data1 = data[1]['BasicSetting']
# data2 = data[0]['login']
# seach = (By.XPATH,data1['seach'])
# seach1 = (By.XPATH, data1['seach1'])
# openSelltext = (By.XPATH,data1['openSelltext'])
# stockmanagement = (By.XPATH,data1['stockmanagement'])
# businessadministration = (By.XPATH, data1['businessadministration'])
# basicsetting = (By.XPATH,data1['basicsetting'])
# basedata = (By.XPATH, data1['basedata'])
# l = []
#
# for i in range(1,10):
#     text = str('//*[@id="clientMain"]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[3]/div')
#     l.append(text)
#     # print(l)
# l = tuple(l)
# print(l[-1])
#
#
#
# '//*[@id="clientMain"]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div'
# '//*[@id="clientMain"]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div'

# # 入库实现
    # @allure.epic("新增采购订单")
    # @allure.feature("新增采购订单测试")
    # @pytest.mark.parametrize('utext', loadyaml('D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver的副本/data/add_Purchasebille.yaml'))
    # def test_2_addPurchasebill(self,utext,init_driver):
    #     '''测试采购订单用例'''
    #     self.ip = Add_Purchasebille(init_driver)
    #     etext = self.ip.add_Purchasebill()
    #     # etext = self.ip.add_Purchasebill(utext['loginurl1'])
    #     pytest.assume(etext == utext['message'] )
    #     # 动态allure标题
    #     allure.dynamic.title(f'{utext["legend"]}')
    #     allure.attach(str([f"{utext['message']} 等于 {etext}"]), "断言信息", allure.attachment_type.TEXT)  # 保存文本为allure的附件
    #     # # 动态allure标题
    #     # allure.dynamic.title(f'搜索商品名称:{utext["search_info"]}')
#
# from selenium import webdriver
# driver.find_element(By.XPATH,
#                                          '//*[@id="app"]/div/section/section/div[1]/ul/li[8]/span/span/div/div/div/span')
# a = Login(driver)
# a.login1()
