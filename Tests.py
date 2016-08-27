import unittest
from selenium import webdriver

# Please input your path to file chromedriver
pathToChromeDriver = "C:\Users\User\PycharmProjects\chromedriver.exe"

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(pathToChromeDriver)
        self.base_url = "http://adat4testers.cleverhosting.org"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/a").click()
        self.driver.implicitly_wait(3)
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("kate")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        my_account = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/div/div").text
        self.assertEquals(my_account, "My Account")

    def test_change_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/a").click()
        self.driver.implicitly_wait(3)
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("kate")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        driver.find_element_by_id("dLabel").click()
        driver.find_element_by_link_text("Account Settings").click()
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/a").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("newpassword").clear()
        driver.find_element_by_name("newpassword").send_keys("123456")
        driver.find_element_by_name("repassword").clear()
        driver.find_element_by_name("repassword").send_keys("123456")
        driver.find_element_by_xpath("//input[@value='Save']").click()
        personal_information = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/div[1]").text
        self.assertEquals(personal_information, "Personal Information")

    def test_change_password_fail(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/a").click()
        self.driver.implicitly_wait(3)
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("kate")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        driver.find_element_by_id("dLabel").click()
        driver.find_element_by_link_text("Account Settings").click()
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/a").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("qwerty")
        driver.find_element_by_name("newpassword").clear()
        driver.find_element_by_name("newpassword").send_keys("123456")
        driver.find_element_by_name("repassword").clear()
        driver.find_element_by_name("repassword").send_keys("123456")
        driver.find_element_by_xpath("//input[@value='Save']").click()
        personal_information = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/div[1]").text
        self.assertEquals(personal_information, "Personal Information")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
