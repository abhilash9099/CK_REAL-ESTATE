import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ll_ATS(unittest.TestCase):

    def setUp(self):
      self.driver = webdriver.Chrome()


    def test_ll(self):
        user = "test"
        pwd = "test123"

        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin")

        # Login process
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(5)

        elem = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')
        elem.click();
        time.sleep(5)
        elem = driver.find_element(By.LINK_TEXT, "Neibhorhoods")
        elem.click();
        elem = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/ul/li/a")
        elem.click();
        time.sleep(5)
        elem = driver.find_element(By.ID, "id_name")
        elem.send_keys("ElkHorn")
        elem = driver.find_element(By.ID, "id_description")
        elem.send_keys("ElkHorn is a beautiful neighbourhood")

        elem = driver.find_element(By.XPATH, '//*[@id="neibhorhood_form"]/div/div/input[1]')
        elem.click();
        time.sleep(5)




    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
