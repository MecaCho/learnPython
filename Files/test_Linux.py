#-*-coding=utf-8-*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_preformance_formal import Performance
from test_render_formal import Render
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    #testunit.addTest(Render("test_Render"))
    testunit.addTest(Performance("test_pre"))
    # test log
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #############################Ubuntu_Share文件下测试用###############################
    testresult_filename = './Test_result/'+'Firefox-35-selenium-2.48.0-'+now+'LinuxPerformanceResult.html'
    fp = open(testresult_filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Linux Render Test Report', description='Test Detail:')
    runner.run(testunit)
    fp.close()

