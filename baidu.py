#-*-coding=utf-8-*-
from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
class test(unittest.TestCase):
    def test_baidu(self):
        driver = webdriver.Ie()
        driver.get("http://www.baidu.com")

        driver.find_element_by_id("kw").send_keys("Selenium2")
        driver.find_element_by_id("su").click()
        driver.quit()

if __name__ == '__main__':
    run_test_baidu = unittest.TestSuite()
    run_test_baidu.addTest(test("test_baidu"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  './' + now +'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='test report',description='test detail:')
    runner.run(run_test_baidu)
    fp.close()
