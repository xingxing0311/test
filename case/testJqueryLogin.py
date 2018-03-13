# coding:utf-8
from selenium import webdriver
import time
import unittest

login_url=r"http://192.168.2.15:8088/adminLogin.jsp"



def execute(driver,location):
    driver.execute_script(location)

class JqurtyLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(login_url)

    def testJquery(self):
        name="$('#userName').val('wuxing')"  #姓名
        execute(self.driver,name)

        password="$('#password').val('123456')" #密码
        execute(self.driver,password)

        verificationCode="$('#verificationCode').val('1234')" #验证码
        execute(self.driver,verificationCode)

        submit="$('#submit').click()" #点击登录
        execute(self.driver,submit)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()


