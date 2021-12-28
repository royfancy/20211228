

from selenium import webdriver

import unittest
from time import sleep


#檢索擺渡搜尋欄
class baidutestcase(unittest.TestCase):
    def setUp(self):
        #用例執行前準備
        #打開瀏覽器
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(10)
        
    def test_baiduselect(self):
        driver=self.driver
        #在搜尋框輸入搜尋內容
        driver.find_element_by_id('kw').send_keys("小貓咪")
        #點擊搜尋
        driver.find_element_by_id('su').click()
        sleep(3)
        
        #斷言  鏈結網頁標題為 小貓咪
        self.assertEqual(self.driver.title,"小貓咪_百度搜索")
        driver.quit()
        
    def test_newslink(self):
        driver1=self.driver
        #點擊擺渡中的新聞
        driver1.find_element_by_css_selector("div#s-top-left a:first-child").click()
        sleep(3)
        #斷言  判斷用例結果
        self.assertEqual(self.driver1.title,"百度新闻——海量中文资讯平台")
        driver1.quit()
        print(self.driver.title)

        

unittest.main()











