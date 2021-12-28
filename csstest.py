
from selenium import webdriver
from time import sleep
#打開瀏覽器
drive=webdriver.Chrome()

#加載相目地址


#定位搜索框
#drive.get("https://www.google.com.tw/")

#sleep(3)
#drive.find_element_by_css_selector("html>body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > input").send_keys("小貓咪")







drive.get("https://www.baidu.com/")
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
sleep(3)

#id定位
#drive.find_element_by_css_selector("#kw").send_keys("小貓咪")


#class定位
#drive.find_element_by_css_selector(".s_ipt").send_keys("小貓咪")


#其他屬性
#drive.find_element_by_css_selector("[autocomplete='off']").send_keys("小貓咪")



#通過多屬性定位
#drive.find_element_by_css_selector("[autocomplete='off'][name='wd']").send_keys("小貓咪")



#通過多屬性定位
#drive.find_element_by_css_selector("[autocomplete='off'][name='wd']").send_keys("小貓咪")



#通過部分屬性值
#drive.find_element_by_css_selector("[autocomplete*='f']").send_keys("小貓咪")
#drive.find_element_by_css_selector("[autocomplete^='of']").send_keys("小貓咪")
#drive.find_element_by_css_selector("[autocomplete$='ff']").send_keys("小貓咪")


#通過層級定位
#drive.find_element_by_css_selector("form>span>input").send_keys("小貓咪")
#drive.find_element_by_css_selector("form#form>span>input").send_keys("小貓咪")#層級和id組合定位
#drive.find_element_by_css_selector("form.fm>span>input").send_keys("小貓咪")#層級和class組合定位


#通過兄弟節點
#drive.find_element_by_css_selector("div#s-top-left a:first-child").click()
drive.find_element_by_css_selector("div#s-top-left>a:nth-child(2)").click()
#drive.find_element_by_css_selector("div#s-top-left>a:last-child").click()



