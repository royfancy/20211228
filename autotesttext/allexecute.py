
import HTMLTestRunner

#unittest默認加載器加載測是用例
import unittest
#discover(目錄路徑，匹配規則)根據匹配規則找指定路徑下文件
testcase_dir="C:\\Users\\user\\Desktop\\autotest\\autotesttext\\testresult\\"

dis=unittest.defaultTestLoader.discover(testcase_dir,"autotest_*.py")#autotest_*.py表示autotest_開頭的所有測試用例


#指定測試告文件
#open(文件名稱，模式)
#模式r w wb wb+
#wb+ 以二進制讀寫方式打開文件，返回文件對象，如果文件存在就覆蓋，否則就創建
test_dir="C:\\Users\\user\\Desktop\\autotest\\autotesttext\\testresult\\report.html"
with open(test_dir,"wb+") as fb:
    


#HTMLTestRunner生成測試報告

    runner=HTMLTestRunner.HTMLTestRunner(stream=fb,title="google測試報告",description="用例執行結果")

#執行測是用例
    runner.run(dis)













