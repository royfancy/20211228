from selenium.webdriver.common.keys import Keys

from selenium import webdriver

import unittest
from time import sleep


#檢索擺渡搜尋欄
class baidutestcase(unittest.TestCase):
    def setUp(self):
        #用例執行前準備
        #打開瀏覽器
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com.tw/")
        self.driver.implicitly_wait(10)
        
    def test_baiduselect(self):
        driver=self.driver
        #在搜尋框輸入搜尋內容
        driver.find_element_by_name("q").send_keys("小貓咪")
        #點擊搜尋
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        sleep(3)
        
        #斷言  鏈結網頁標題為 小貓咪
        self.assertEqual(self.driver.title,"小貓咪 - Google 搜尋")
        
        
    def test_newslink(self):
        driver=self.driver
        #點擊擺渡中的新聞
        driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.n1xJcf.Ne6nSd > a:nth-child(2)").click()
        sleep(3)
        #斷言  判斷用例結果
        self.assertEqual(self.driver.title,"Google - 關於")
        
    def testDown(self):
        self.driver.quit()

        

unittest.main()













