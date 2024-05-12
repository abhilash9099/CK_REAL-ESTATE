import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        user = "test"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")

        elem = driver.find_element(By.LINK_TEXT, "Login")
        elem.click()

        driver.find_element(By.ID, "id_username").send_keys(user)
        driver.find_element(By.ID,"id_password").send_keys(pwd)

        elem = driver.find_element(By.ID, "login")
        elem.click()

        try:
            # attempt to find the 'Login' button - if not found, that means login worked
            elem = driver.find_element(By.LINK_TEXT, "Login")
            time.sleep(3)
            driver.close()
            self.fail("Login Failed - as login button still visible")

        except NoSuchElementException:
            driver.close()
            self.assertTrue(True, "Login Succeded - user does exist")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
