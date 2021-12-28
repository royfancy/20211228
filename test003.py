# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:50:53 2021

@author: user
"""

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest, time

# d=webdriver.Firefox()
# d.get("http://www.baidu.com")


class BaiduIdeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def test_baidu_ide(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        time.sleep(5)
        self.assertEqual("HTMLTestRunner_百度搜尋", driver.title)
        print(driver.title)
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # 構造測試套件
    testsuit = unittest.TestSuite()
    testsuit.addTest(BaiduIdeTest("test_baidu_ide"))
    # 定義測試報告存放路徑
    with open('./result.html', 'wb') as fp:
        
    # 定義測試報告
        runner = HTMLTestRunner(stream=fp,
                            title='自動化測試報告',
                            description='用例執行情況：')
        runner.run(testsuit)
    # 關閉測試報告
    