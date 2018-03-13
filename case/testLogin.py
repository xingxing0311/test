# coding:utf-8
from selenium import webdriver
import unittest
login_url=r"http://192.168.2.15:8088/adminLogin.jsp"
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get(login_url)
        self.driver.maximize_window()
    def testTrue(self):
        u'''输入正确的账号密码'''
        name="wuxing"
        password="123456"
        time.sleep(2)
        self.driver.find_element_by_id("userName").send_keys(name)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("verificationCode").send_keys("1232")
        self.driver.find_element_by_id("submit").click()
        try:
            time.sleep(3)
            nick_name=self.driver.find_element_by_id("adminName").text
            print nick_name
            print u"登录成功"
        except:
            nick_name="1111"
            print u"登录失败"
        self.assertEqual(name, nick_name)

    def testFalse(self):
        u'''输入错误的账号密码'''
        name = "wuxing12"
        password = "123456"
        self.driver.find_element_by_id("userName").send_keys(name)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("verificationCode").send_keys("1232")
        self.driver.find_element_by_id("submit").click()
        alert_text=self.driver.switch_to_alert().text
        alert_text_string=alert_text.encode("utf-8")
        alert_text_show="用户信息不存在"
        self.assertIn(alert_text_show,alert_text_string)

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()