from selenium import webdriver
from locators import LoginPage, CreateAccountPage
import time
import unittest

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('D:/GITHUB/begin_selenium_python-course/chromedriver')
        self.addCleanup(self.browser.quit)

    def testUserLogin(self):
        # Happy Path - Login Success
        self.browser.get('http://localhost:8000/Section%204%20Code/4.4/')
        # print(LoginPage.username_field)
        username = self.browser.find_element(*LoginPage.username_field)
        password = self.browser.find_element(*LoginPage.password_field)
        # print(*LoginPage.password_field)
        # print(password)
        submit = self.browser.find_element(*LoginPage.submit_btn)
        username.send_keys('registeredUser')
        password.send_keys('1234')
        submit.click()
        time.sleep(2)
        welcome_message = self.browser.find_element(*LoginPage.message)
        self.assertIn('Welcome back', welcome_message.text)

    def testLoginFail(self):
        self.browser.get('http://localhost:8000/Section%204%20Code/4.4/')
        username = self.browser.find_element(*LoginPage.username_field)
        password = self.browser.find_element(*LoginPage.password_field)
        submit = self.browser.find_element(*LoginPage.submit_btn)
        username.send_keys('otherUser')
        password.send_keys('asdf')
        submit.click()
        time.sleep(2)
        message = self.browser.find_element(*LoginPage.message)
        self.assertIn('Account not found', message.text)
        create_account_link = self.browser.find_element(*LoginPage.create_acct_link)
        create_account_link.click()
        time.sleep(2)
        header = self.browser.find_element(*CreateAccountPage.header)
        self.assertIn('Create an Account', header.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
